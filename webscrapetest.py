import pandas as pd
import requests
from bs4 import BeautifulSoup
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
import os

df = pd.read_parquet("logos.snappy(1).parquet")

numLogos = int(input("Enter the number of logos to scrape and compare: "))
if numLogos > len(df):
    print(f"Warning: Only {len(df)} logos are available. Scraping all.")
    numLogos = len(df)

os.makedirs("logos", exist_ok=True)

def extractLogoUrl(domain):
    try:
        url = f"https://{domain}"
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        logoTag = soup.find("img", class_=lambda x: x and "logo" in x.lower())
        if logoTag:
            logoUrl = logoTag["src"]
            if not logoUrl.startswith("http"):
                logoUrl = f"https://{domain}{logoUrl}"
            return logoUrl
    except Exception as e:
        print(f"Error extracting logo from {domain}: {e}")
    return None

def downloadLogo(logoUrl, savePath):
    try:
        response = requests.get(logoUrl, timeout=10)
        response.raise_for_status()
        with open(savePath, "wb") as f:
            f.write(response.content)
        print(f"Downloaded: {logoUrl}")
    except Exception as e:
        print(f"Failed to download {logoUrl}: {e}")

imagePaths = []
for index in range(numLogos):
    domain = df.iloc[index]["domain"]
    logoUrl = extractLogoUrl(domain)
    if logoUrl:
        savePath = f"logos/logo_{index}.png"
        downloadLogo(logoUrl, savePath)
        imagePaths.append(savePath)
    else:
        print(f"No logo found for {domain}")

images = []
for path in imagePaths:
    img = cv2.imread(path)
    if img is not None:
        img = cv2.resize(img, (100, 100))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        images.append(img)
    else:
        print(f"Failed to load: {path}")

images = np.array(images)
print("Images array shape:", images.shape)

def computeHistogram(img):
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    hist = cv2.normalize(hist, hist).flatten()
    return hist

def compareHistograms(hist1, hist2):
    return cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

def histogramSimilarity(images):
    num = len(images)
    simMatrix = np.zeros((num, num))
    hists = [computeHistogram(img) for img in images]
    for i in range(num):
        for j in range(num):
            simMatrix[i, j] = compareHistograms(hists[i], hists[j])
    return simMatrix

def ssimSimilarity(images):
    num = len(images)
    simMatrix = np.zeros((num, num))
    for i in range(num):
        for j in range(num):
            if i == j:
                simMatrix[i, j] = 1.0
            else:
                simMatrix[i, j] = ssim(images[i], images[j])
    return simMatrix

def combineMatrices(matrices, weights):
    combined = np.zeros_like(matrices[0])
    for mat, weight in zip(matrices, weights):
        combined += mat * weight
    return combined

def groupImages(simMatrix, threshold=0.75):
    num = len(simMatrix)
    groups = []
    visited = set()
    for i in range(num):
        if i not in visited:
            group = [i]
            for j in range(i + 1, num):
                if simMatrix[i, j] > threshold:
                    group.append(j)
                    visited.add(j)
            groups.append(group)
    return groups

def showGroups(groups, images):
    for group in groups:
        if len(group) > 1:
            print(f"Group: {group}")
            resized = []
            for idx in group:
                imgBgr = cv2.cvtColor(images[idx], cv2.COLOR_GRAY2BGR)
                imgResized = cv2.resize(imgBgr, (400, 400))
                resized.append(imgResized)
            combined = np.hstack(resized)
            cv2.imshow(f"Group {group}", combined)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

if len(images) > 0:
    histSim = histogramSimilarity(images)
    ssimSim = ssimSimilarity(images)

    combinedSim = combineMatrices([histSim, ssimSim], [0.4, 0.6])
    print("Combined Similarity Matrix:")
    print(combinedSim)

    groups = groupImages(combinedSim, threshold=0.2)
    print("Groups of similar images:")
    print(groups)

    showGroups(groups, images)
else:
    print("No images loaded.")