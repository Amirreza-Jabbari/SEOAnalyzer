# SEOAnalyzer Documentation

## Table of Contents
1. [Overview](#overview)
2. [Dependencies](#dependencies)
3. [Class: SEOAnalyzer](#class-seoanalyzer)
   - [Initialization](#initialization)
   - [Methods](#methods)
     - [analyze_page_speed(url)](#analyze_page_speedurl)
     - [extract_resources(html_content, base_url)](#extract_resourceshtml_content-base_url)
     - [resolve_url(resource_url, base_url)](#resolve_urlresource_url-base_url)
     - [analyze_resource_load_times(resources)](#analyze_resource_load_timesresources)
     - [speed_optimization_suggestions(speed_data)](#speed_optimization_suggestionsspeed_data)
     - [calculate_performance_score(load_time, page_size)](#calculate_performance_scoreload_time-page_size)
     - [check_mobile_friendly(html_content)](#check_mobile_friendlyhtml_content)
     - [check_https(response)](#check_httpsresponse)
     - [check_page_title(html_content)](#check_page_titlehtml_content)
     - [check_meta_description(html_content)](#check_meta_descriptionhtml_content)
     - [analyze_header_structure(html_content)](#analyze_header_structurehtml_content)
     - [analyze_internal_links(html_content, base_url)](#analyze_internal_linkshtml_content-base_url)
     - [analyze_external_links(content, url)](#analyze_external_linkscontent-url)
     - [check_image_alt_text(html_content)](#check_image_alt_texthtml_content)
     - [check_broken_internal_links(html_content, base_url)](#check_broken_internal_linkshtml_content-base_url)
     - [check_xml_sitemap(base_url)](#check_xml_sitemapbase_url)
     - [check_robots_txt(base_url)](#check_robots_txtbase_url)
     - [check_canonical_tags(html_content)](#check_canonical_tagshtml_content)
     - [check_content_freshness(html_content)](#check_content_freshnesshtml_content)
     - [log_broken_link(url)](#log_broken_linkurl)
     - [analyze_keyword_density(text)](#analyze_keyword_densitytext)
     - [assess_content_quality(text)](#assess_content_qualitytext)
     - [semantic_analysis(text)](#semantic_analysistext)
     - [competitor_analysis(competitor_url)](#competitor_analysiscompetitor_url)
     - [check_broken_links(urls)](#check_broken_linksurls)
     - [local_seo_analysis(html_content)](#local_seo_analysishtml_content)
     - [core_web_vitals_check(url)](#core_web_vitals_checkurl)
     - [generate_performance_recommendations(speed_data)](#generate_performance_recommendationsspeed_data)
     - [compress_image(input_image_path, output_image_path, quality=80)](#compress_imageinput_image_path-output_image_path-quality80)
     - [plot_seo_scores(current_scores, historical_scores)](#plot_seo_scorescurrent_scores-historical_scores)
4. [Example Usage](#example-usage)
5. [Conclusion](#conclusion)
6. [License](#license)

## Overview
The `SEOAnalyzer` class provides a comprehensive set of tools for analyzing and optimizing website SEO metrics. It focuses on various aspects of SEO, including page speed, content quality, link integrity, and social media presence. The class employs several libraries such as `requests`, `BeautifulSoup`, `spaCy`, and `matplotlib` to gather, analyze, and visualize SEO data.

## Dependencies
The following Python libraries are required to run the `SEOAnalyzer`:
- `requests`: For making HTTP requests.
- `BeautifulSoup (bs4)`: For parsing HTML and extracting data.
- `spaCy`: For natural language processing tasks.
- `matplotlib`: For plotting graphs.
- `Pillow`: For image manipulation.
- `numpy`: For numerical operations.

## Class: SEOAnalyzer
### Initialization
```python
def __init__(self):
    self.nlp = spacy.load("en_core_web_sm")  # Load the SpaCy model
    self.broken_links_log = []  # Initialize broken links log
```
This constructor initializes the `SEOAnalyzer` class by loading the SpaCy model for natural language processing and creating a list to log broken links.

### Methods

#### analyze_page_speed(url)
Analyzes the page speed and various SEO metrics of the specified URL.

**Parameters:**
- `url` (str): The URL of the webpage to analyze.

**Returns:**
- dict: A dictionary containing various SEO metrics and analysis results.

#### extract_resources(html_content, base_url)
Extracts resources (CSS, JavaScript, and images) from the HTML content.

**Parameters:**
- `html_content` (str): The HTML content of the page.
- `base_url` (str): The base URL for resolving relative URLs.

**Returns:**
- dict: A dictionary with lists of extracted CSS, JS, and image URLs.

...

#### plot_seo_scores(current_scores, historical_scores)
Plots a comparison of current and historical SEO scores.

**Parameters:**
- `current_scores` (dict): A dictionary containing current SEO scores.
- `historical_scores` (dict): A dictionary containing historical SEO scores.

**Returns:**
- None

## Example Usage
```python
seo_analyzer = SEOAnalyzer()
url = "https://example.com"
result = seo_analyzer.analyze_page_speed(url)
print(result)
```

## Conclusion
The `SEOAnalyzer` class is a powerful tool for webmasters and SEO professionals looking to improve their website's search engine optimization. By utilizing various methods for analyzing different aspects of SEO, users can gain valuable insights and make informed decisions to enhance their online presence.

## License
MIT License

```
MIT License

Copyright (c) 2024 Amirreza Jabbari

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```