<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Logo Clustering Project</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 40px; }
        h1, h2 { color: #333; }
        code { background: #f4f4f4; padding: 5px; border-radius: 4px; }
        pre { background: #f4f4f4; padding: 10px; border-radius: 4px; overflow-x: auto; }
    </style>
</head>
<body>
    <h1>Logo Clustering Project</h1>
    <p>This project extracts, downloads, and compares logos from company websites using <strong>OpenCV, BeautifulSoup, Pandas, and NumPy</strong>. The logos are clustered based on structural similarity and histogram comparison.</p>

    <h2>Features</h2>
    <ul>
        <li>Extracts logos from website domains.</li>
        <li>Downloads and processes logos using OpenCV.</li>
        <li>Compares logos using histogram correlation and SSIM.</li>
        <li>Groups similar logos based on computed similarity scores.</li>
    </ul>

    <h2>Installation</h2>
    <pre><code>pip install -r requirements.txt</code></pre>

    <h2>Usage</h2>
    <pre><code>python script.py</code></pre>

    <h2>How It Works</h2>
    <ol>
        <li>Reads company domains from a <code>parquet</code> file.</li>
        <li>Scrapes the website to find the logo.</li>
        <li>Downloads and processes the logo images.</li>
        <li>Resizes images to 100x100 and converts them to grayscale.</li>
        <li>Compares images using histogram correlation and SSIM.</li>
        <li>Groups similar images and displays them.</li>
    </ol>

    <h2>Similarity Calculation</h2>
    <p>The similarity matrix is computed using:</p>
    <ul>
        <li><strong>Histogram Comparison:</strong> Measures color distribution similarity.</li>
        <li><strong>SSIM (Structural Similarity Index):</strong> Measures structural resemblance.</li>
        <li><strong>Combined Matrix:</strong> Weighted sum of histogram and SSIM similarity matrices.</li>
    </ul>

    <h2>Output</h2>
    <p>The program outputs groups of websites with similar logos and displays them side by side.</p>

    <h2>Example</h2>
    <pre><code>Enter the number of logos to scrape and compare: 10
Downloaded: example.com/logo.png
Groups of similar images: [[0, 2, 5], [1, 3], [4, 6, 7]]</code></pre>

    <h2>Contributing</h2>
    <p>Feel free to fork this project and improve it!</p>

    <h2>License</h2>
    <p>This project is licensed under the MIT License.</p>
</body>
</html>
