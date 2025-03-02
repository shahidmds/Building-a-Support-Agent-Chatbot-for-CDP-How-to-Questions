import httpx
from bs4 import BeautifulSoup
import json
import time
from urllib.parse import urljoin, urlparse

# Documentation URLs to scrape
DOC_URLS = {
    "Segment": "https://segment.com/docs/",
    "mParticle": "https://docs.mparticle.com/",
    "Lytics": "https://docs.lytics.com/",
    "Zeotap": "https://docs.zeotap.com/home/en-us/"
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

MAX_DEPTH = 0  # Prevents infinite recursion

def scrape_page(url, visited, depth=0):
    """Scrapes text content from a single webpage and follows internal links."""
    if url in visited or depth > MAX_DEPTH:
        return ""
    
    print(f"🔍 Scraping: {url} (Depth: {depth})")
    visited.add(url)

    try:
        response = httpx.get(url, headers=HEADERS, timeout=10)
        if response.status_code != 200:
            print(f"❌ Failed to fetch {url} (Status Code: {response.status_code})")
            return ""
        
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract main text content
        text_content = " ".join([p.get_text(strip=True) for p in soup.find_all("p")])

        # Extract and follow internal links
        domain = urlparse(url).netloc
        for link in soup.find_all("a", href=True):
            absolute_link = urljoin(url, link["href"])
            if urlparse(absolute_link).netloc == domain:  # Only follow links within the same domain
                text_content += "\n" + scrape_page(absolute_link, visited, depth + 1)

        return text_content

    except httpx.RequestError as e:
        print(f"❌ Error fetching {url}: {e}")
        return ""

def scrape_docs():
    """Scrapes all main documentation pages and their linked pages."""
    scraped_data = {}

    for name, url in DOC_URLS.items():
        visited_links = set()
        scraped_data[name] = scrape_page(url, visited_links)

    # Save data to a file
    with open("scraped_docs.json", "w", encoding="utf-8") as f:
        json.dump(scraped_data, f, indent=4)

    print("🎉 Scraping completed!")

if __name__ == "__main__":
    scrape_docs()
