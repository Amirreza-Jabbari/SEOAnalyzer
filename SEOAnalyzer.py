import requests
import json
import spacy
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
from sklearn.feature_extraction.text import CountVectorizer
from urllib.parse import urlparse
import re
import logging
import time
from bs4 import BeautifulSoup
import os
from urllib.parse import urlparse
import numpy as np

# Setup logging
logging.basicConfig(level=logging.INFO)

class SEOAnalyzer:

    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")  # Load the SpaCy model
        self.broken_links_log = []  # Initialize broken links log

    def analyze_page_speed(self, url):
        try:
            # Start measuring time
            start_time = time.time()

            # Make the initial request to get the HTML
            response = requests.get(url)
            response.raise_for_status()

            # Total load time
            total_load_time = time.time() - start_time
            
            # Analyzing response headers for performance metrics
            server_response_time = float(response.elapsed.total_seconds())
            page_size = len(response.content) / 1024  # Size in KB

            # Extracting resources
            resources = self.extract_resources(response.text, url)

            # Analyzing resource load times
            resource_times = self.analyze_resource_load_times(resources)

            # Analyze content quality and keyword density
            content = response.text
            keyword_density = self.analyze_keyword_density(content)
            content_quality = self.assess_content_quality(content)

            # Analyze social media tags
            social_media = self.social_media_analysis(content)

            # Analyze schema markup
            schema_info = self.rich_content_analysis(content)

            # Constructing the final report
            report = {
                "URL": url,
                "Total Load Time (seconds)": total_load_time,
                "Server Response Time (seconds)": server_response_time,
                "Page Size (KB)": page_size,
                "Resource Load Times": resource_times,
                "Performance Score": self.calculate_performance_score(total_load_time, page_size),
                "Mobile Friendliness": self.check_mobile_friendly(response.text),
                "HTTPS Check": self.check_https(response),
                "Page Title": self.check_page_title(response.text),
                "Meta Description": self.check_meta_description(response.text),
                "Header Structure": self.analyze_header_structure(response.text),
                "Internal Links": self.analyze_internal_links(response.text, url),
                "External Links": self.analyze_external_links(content, url),
                "Image Alt Text": self.check_image_alt_text(response.text),
                "Broken Internal Links": self.check_broken_internal_links(response.text, url),
                "XML Sitemap": self.check_xml_sitemap(url),
                "Robots.txt": self.check_robots_txt(url),
                "Canonical Tags": self.check_canonical_tags(response.text),
                "Schema Markup": self.check_schema_markup(response.text),
                "Content Freshness": self.check_content_freshness(response.text),
                "Keyword Density": self.analyze_keyword_density(response.text),
                "Content Quality": self.assess_content_quality(response.text),
                "Social Media Analysis": self.social_media_analysis(response.text),
                "Rich Content Analysis": self.rich_content_analysis(response.text),
                "SEO Suggestions": self.speed_optimization_suggestions({
                    "Total Load Time (seconds)": total_load_time,
                    "Page Size (KB)": page_size
                }),
                "Local SEO Analysis": self.local_seo_analysis(response.text),
                "Competitor Analysis": self.competitor_analysis("https://competitor.com"),
                "404 Errors": self.analyze_404_errors(self.analyze_internal_links(response.text, url)),
                "Broken Links": self.check_broken_links(self.analyze_internal_links(response.text, url)),
            }

            return report

        except requests.exceptions.RequestException as e:
            return {"error": str(e)}


    def extract_resources(self, html_content, base_url):
        soup = BeautifulSoup(html_content, 'html.parser')
        resources = {
            "css": [],
            "js": [],
            "images": []
        }
        
        # Extract CSS files
        for link in soup.find_all('link', rel='stylesheet'):
            css_url = link.get('href')
            if css_url:
                resources["css"].append(self.resolve_url(css_url, base_url))
        
        # Extract JS files
        for script in soup.find_all('script'):
            js_url = script.get('src')
            if js_url:
                resources["js"].append(self.resolve_url(js_url, base_url))
        
        # Extract images
        for img in soup.find_all('img'):
            img_url = img.get('src')
            if img_url:
                resources["images"].append(self.resolve_url(img_url, base_url))
        
        return resources

    def resolve_url(self, resource_url, base_url):
        if urlparse(resource_url).netloc:
            return resource_url
        else:
            return requests.compat.urljoin(base_url, resource_url)

    def analyze_resource_load_times(self, resources):
        resource_times = {}
        for resource_type, urls in resources.items():
            load_times = []
            for url in urls:
                start_time = time.time()
                try:
                    requests.get(url, timeout=5)  # Simulating load time
                except requests.exceptions.RequestException:
                    load_times.append(None)  # Resource failed to load
                load_times.append(time.time() - start_time)
            resource_times[resource_type] = load_times
        return resource_times
    
    def speed_optimization_suggestions(self, speed_data):
        """
        Provide suggestions for improving page loading speed based on the speed data.
        """
        recommendations = []
        
        if speed_data['Total Load Time (seconds)'] > 2:
            recommendations.append("Consider optimizing images and using lazy loading.")
        if speed_data['Page Size (KB)'] > 100:
            recommendations.append("Minimize CSS and JavaScript files.")
        
        return recommendations

    def calculate_performance_score(self, load_time, page_size):
        if load_time < 2:
            return 100 - (load_time * 10) - (page_size / 100)
        else:
            return max(0, 100 - (load_time * 15) - (page_size / 50))
        

    def check_mobile_friendly(self, html_content):
        # Placeholder logic for mobile friendliness
        return "Yes" if '<meta name="viewport"' in html_content else "No"

    def check_https(self, response):
        return "Yes" if response.url.startswith('https://') else "No"

    def check_page_title(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        title = soup.title.string if soup.title else "Missing"
        return title

    def check_meta_description(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        description = soup.find('meta', attrs={'name': 'description'})
        return description['content'] if description else "Missing"

    def analyze_header_structure(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        headers = {
            "H1 Count": len(soup.find_all('h1')),
            "H2 Count": len(soup.find_all('h2')),
            "H3 Count": len(soup.find_all('h3'))
        }
        return headers
    
    def analyze_internal_links(self, html_content, base_url):
        soup = BeautifulSoup(html_content, 'html.parser')
        internal_links = []
        for link in soup.find_all('a', href=True):
            if self.resolve_url(link['href'], base_url).startswith(base_url):
                internal_links.append(link['href'])
        return internal_links

    def analyze_external_links(self, content, url):
        # Parse the content with BeautifulSoup
        soup = BeautifulSoup(content, 'html.parser')
        
        links = soup.find_all('a', href=True)  # Find all anchor tags with href
        external_links = []

        for link in links:
            link_href = link['href']
            # Check if the link is external
            if urlparse(link_href).netloc != urlparse(url).netloc:
                external_links.append(link_href)

        return external_links

    def check_image_alt_text(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        images = soup.find_all('img')
        missing_alt = [img['src'] for img in images if not img.get('alt')]
        return missing_alt if missing_alt else "All images have alt text"

    def check_broken_internal_links(self, html_content, base_url):
        internal_links = self.analyze_internal_links(html_content, base_url)
        broken_links = []
        for link in internal_links:
            try:
                response = requests.head(self.resolve_url(link, base_url))
                if response.status_code != 200:
                    broken_links.append(link)
                    self.log_broken_link(link)
            except requests.exceptions.RequestException:
                broken_links.append(link)
                self.log_broken_link(link)
        return broken_links

    def check_xml_sitemap(self, base_url):
        sitemap_url = requests.compat.urljoin(base_url, '/sitemap.xml')
        try:
            response = requests.head(sitemap_url)
            return "Exists" if response.status_code == 200 else "Not Found"
        except requests.exceptions.RequestException:
            return "Error fetching"

    def check_robots_txt(self, base_url):
        robots_url = requests.compat.urljoin(base_url, '/robots.txt')
        try:
            response = requests.get(robots_url)
            return response.text if response.status_code == 200 else "Not Found"
        except requests.exceptions.RequestException:
            return "Error fetching"

    def check_canonical_tags(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        canonical = soup.find('link', rel='canonical')
        return canonical['href'] if canonical else "Missing"

    def check_content_freshness(self, html_content):
        # Placeholder logic for checking content freshness
        last_modified = re.search(r'<meta name="last-modified" content="(.*?)"', html_content)
        return last_modified.group(1) if last_modified else "Not Found"

    def log_broken_link(self, url):
        logging.warning(f"Broken link detected: {url}")
        self.broken_links_log.append(url)

    def analyze_keyword_density(self, text):
        doc = self.nlp(text)
        keywords = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
        vectorizer = CountVectorizer()
        X = vectorizer.fit_transform([' '.join(keywords)])
        keyword_freq = dict(zip(vectorizer.get_feature_names_out(), X.toarray()[0]))
        return keyword_freq

    def assess_content_quality(self, text):
        doc = self.nlp(text)
        return {
            "Word Count": len(doc),
            "Sentiment Score": doc._.polarity if hasattr(doc._, 'polarity') else 0
        }

    def semantic_analysis(self, text):
        doc = self.nlp(text)
        topics = set(token.lemma_ for token in doc if token.pos_ in ['NOUN', 'PROPN'])
        return {
            "Topics Detected": list(topics),
            "Topic Count": len(topics)
        }

    def competitor_analysis(self, competitor_url):
        """
        Analyze competitor's SEO metrics.
        This is a placeholder and should be integrated with an actual SEO API or tool.
        """
        # Placeholder data for demonstration
        backlinks = 150  # Mock data
        keywords = ["example keyword", "another keyword"]  # Mock data
        estimated_traffic = 5000  # Mock data

        return {
            "Competitor URL": competitor_url,
            "Backlinks": backlinks,
            "Keywords": keywords,
            "Estimated Traffic": estimated_traffic
        }


    def check_broken_links(self, urls):
        broken_links = []
        for url in urls:
            try:
                response = requests.head(url, allow_redirects=True)
                if response.status_code != 200:
                    broken_links.append(url)
                    self.log_broken_link(url)
            except requests.exceptions.RequestException:
                broken_links.append(url)
                self.log_broken_link(url)
        return broken_links
    

    def local_seo_analysis(self, html_content):
        name = re.search(r'<meta name="name" content="(.*?)"', html_content)
        address = re.search(r'<meta name="address" content="(.*?)"', html_content)
        phone = re.search(r'<meta name="phone" content="(.*?)"', html_content)

        return {
            "Name": name.group(1) if name else "Missing",
            "Address": address.group(1) if address else "Missing",
            "Phone": phone.group(1) if phone else "Missing"
        }

    def core_web_vitals_check(self, url):
        speed_data = self.fetch_speed_data(url)
        recommendations = self.generate_performance_recommendations(speed_data)
        return {
            "Performance Score": speed_data['Performance Score'],
            "Core Web Vitals": speed_data['Metrics'],
            "Recommendations": recommendations
        }
    
    def generate_performance_recommendations(self, speed_data):
        recommendations = []
        if speed_data['Performance Score'] < 50:
            recommendations.append("Consider optimizing images and minimizing JavaScript.")
        return recommendations

    def compress_image(self, input_image_path, output_image_path, quality=80):
        try:
            with Image.open(input_image_path) as img:
                img.save(output_image_path, "JPEG", quality=quality)
            return f"Image saved at {output_image_path} with {quality}% quality."
        except Exception as e:
            logging.error(f"Error compressing image: {e}")
            return str(e)

    def plot_seo_scores(self, current_scores, historical_scores):
        labels = list(current_scores.keys())
        current_values = list(current_scores.values())
        historical_values = list(historical_scores.values())

        x = range(len(labels))

        plt.plot(x, current_values, marker='o', label='Current')
        plt.plot(x, historical_values, marker='x', label='Historical')

        plt.xticks(x, labels)
        plt.xlabel('Metrics')
        plt.ylabel('Scores')
        plt.title('SEO Scores Comparison')
        plt.legend()
        plt.grid()
        plt.show()

    def continuous_monitoring(self, url):
        """
        Monitor the SEO status of the URL and log changes.
        This implementation uses a JSON file to store historical data.
        """
        historical_data_file = 'historical_data.json'
        
        # Load previous data if exists
        previous_data = {}
        if os.path.exists(historical_data_file):
            with open(historical_data_file, 'r') as file:
                previous_data = json.load(file)

        current_data = self.analyze_page_speed(url)
        
        # Check if the URL is already in historical data
        if url not in previous_data:
            previous_data[url] = {
                "Total Load Time (seconds)": current_data["Total Load Time (seconds)"],
                "Server Response Time (seconds)": current_data["Server Response Time (seconds)"],
                "Page Size (KB)": current_data["Page Size (KB)"]
            }
        else:
            # Compare with historical data
            if (current_data['Total Load Time (seconds)'] != previous_data[url]['Total Load Time (seconds)'] or
                    current_data['Server Response Time (seconds)'] != previous_data[url]['Server Response Time (seconds)'] or
                    current_data['Page Size (KB)'] != previous_data[url]['Page Size (KB)']):
                logging.info(f"Change detected in SEO metrics for {url}: {current_data}")
                # Update historical data with current data
                previous_data[url].update(current_data)

        # Save updated historical data
        with open(historical_data_file, 'w') as file:
            json.dump(previous_data, file, indent=4)

    def analyze_404_errors(self, url_list):
        """
        Check for 404 errors on the given URLs and return a report.
        """
        error_404s = []
        for url in url_list:
            try:
                response = requests.head(url)
                if response.status_code == 404:
                    error_404s.append(url)
                    logging.warning(f"404 Error detected for URL: {url}")
            except requests.exceptions.RequestException:
                logging.error(f"Error checking URL: {url}")

        return error_404s

    def rich_content_analysis(self, content):
        schema_data = self.check_schema_markup(content)  # Ensure the method name is correct

        return {
            "Schema Types Found": schema_data['Schema Types Found'],  # Ensure this key exists in schema_data
            # Add other relevant data from schema_data
        }
    
    def check_schema_markup(self, content):
        # Example implementation: This should analyze the content and return the relevant schema types
        soup = BeautifulSoup(content, 'html.parser')
        
        # For demonstration, let's say we want to check for a specific schema type in the content
        schema_types = []

        # This is just a placeholder logic; adjust it based on your actual requirements
        if "Article" in content:
            schema_types.append("Article")
        if "WebSite" in content:
            schema_types.append("WebSite")
        
        return {
            'Schema Types Found': schema_types  # Ensure this is a list or other iterable
        }

    def smart_suggestions(self, html_content):
        website_type = self.detect_website_type(html_content)
        suggestions = []
        
        if website_type == "E-commerce":
            suggestions.extend([
                "Optimize product images for faster loading.",
                "Ensure proper category structure for products.",
                "Implement user reviews for better engagement.",
                "Add related products to enhance upselling."
            ])
        elif website_type == "Blog":
            suggestions.extend([
                "Use header tags for better content structure.",
                "Optimize blog post images with alt tags.",
                "Implement internal linking for related posts.",
                "Encourage comments for user engagement."
            ])
        return suggestions

    def detect_website_type(self, html_content):
        if "product" in html_content.lower():
            return "E-commerce"
        elif "<article>" in html_content or "<blog>" in html_content:
            return "Blog"
        return "Other"
    
    def social_media_analysis(self, html_content):
        """
        Analyze social media tags and their presence.
        """
        og_image = re.search(r'property="og:image" content="(.*?)"', html_content)
        twitter_image = re.search(r'name="twitter:image" content="(.*?)"', html_content)

        return {
            "Open Graph Image": og_image.group(1) if og_image else "Missing",
            "Twitter Image": twitter_image.group(1) if twitter_image else "Missing"
        }
    
    

    def keyword_analysis(self, text):
        """
        Perform a deeper analysis of keyword usage and opportunities.
        """
        doc = self.nlp(text)
        keywords = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
        keyword_freq = {keyword: keywords.count(keyword) for keyword in set(keywords)}
        
        return keyword_freq
    
def convert_to_standard(data):
    if isinstance(data, np.integer):  # Check for NumPy integer types
        return int(data)
    elif isinstance(data, (float, np.float64)):  # Use built-in float and np.float64 for NumPy floats
        return float(data)
    elif isinstance(data, list):
        return [convert_to_standard(item) for item in data]
    elif isinstance(data, dict):
        return {key: convert_to_standard(value) for key, value in data.items()}
    return data

# Example usage
analyzer = SEOAnalyzer()
url = 'https://example.com/'
report = analyzer.analyze_page_speed(url)

# Convert report to a JSON-serializable format
report = convert_to_standard(report)

print(json.dumps(report, indent=2))
