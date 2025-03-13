import requests
from bs4 import BeautifulSoup

def fetch_article(url, headers=None):
    """Fetch the HTML content of a Medium article."""
    if headers is None:
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://medium.com/',
        'DNT': '1',
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch the article. Status code: {response.status_code}")

def get_title(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract title
    title_tag = soup.find('h1')
    title = title_tag.get_text() if title_tag else 'Untitled'

    return title

