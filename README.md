
<body>
    <h1>Logo Similarity Task</h1>
    <p>This program extracts logos from websites, processes them, and compares their similarity using computer vision techniques.</p>

<h2>How It Works</h2>
    <ol>
        <li><strong>Input: Company Domains</strong>
            <ul>
                <li>Reads a list of company domains from a <code>parquet</code> file.</li>
            </ul>
        </li>
        <li><strong>Logo Extraction</strong>
            <ul>
                <li>Scrapes the website to find the logo by searching for common HTML tags (e.g., <code>&lt;img&gt;</code>).</li>
                <li>Extracts the logo URL from the website's HTML.</li>
            </ul>
        </li>
        <li><strong>Logo Download and Preprocessing</strong>
            <ul>
                <li>Downloads the logo image from the extracted URL.</li>
                <li>Resizes the image to a fixed size (e.g., 100x100 pixels).</li>
                <li>Converts the image to grayscale for consistency.</li>
            </ul>
        </li>
        <li><strong>Similarity Calculation</strong>
            <ul>
                <li><strong>Histogram Comparison</strong>: Measures the similarity of pixel intensity distributions.</li>
                <li><strong>SSIM (Structural Similarity Index)</strong>: Measures structural resemblance between images.</li>
                <li><strong>Combined Similarity Matrix</strong>: Combines histogram and SSIM scores into a single similarity matrix.</li>
            </ul>
        </li>
        <li><strong>Grouping Similar Logos</strong>
            <ul>
                <li>Groups logos based on their similarity scores.</li>
                <li>Applies a threshold to determine if logos are similar.</li>
            </ul>
        </li>
        <li><strong>Output</strong>
            <ul>
                <li>Outputs groups of similar logos.</li>
                <li>Displays grouped logos side by side for visual comparison.</li>
            </ul>
        </li>
    </ol>

<h2>Example Workflow</h2>
    <pre><code>1. Input: A list of domains (e.g., example.com, example.org, example.net).
2. Logo Extraction: Scrapes each website and extracts the logo URL.
3. Download and Preprocess: Logos are downloaded, resized, and converted to grayscale.
4. Similarity Calculation: Computes histogram correlation and SSIM for each pair of logos.
5. Grouping: Logos are grouped based on similarity scores.
6. Output: Groups of similar logos are displayed.</code></pre>

<h2>Key Technologies Used</h2>
    <ul>
        <li><strong>Web Scraping</strong>: To extract logo URLs from websites.</li>
        <li><strong>OpenCV</strong>: For image processing (resizing, grayscale conversion, histogram calculation).</li>
        <li><strong>SSIM</strong>: For structural similarity comparison.</li>
        <li><strong>Clustering Algorithms</strong>: To group similar logos based on similarity scores.</li>
    </ul>

<h2>Applications</h2>
    <ul>
        <li><strong>Brand Monitoring</strong>: Identify websites using similar or identical logos.</li>
        <li><strong>Logo Recognition</strong>: Detect logos in a large dataset of images.</li>
    </ul>
</body>
</html>
