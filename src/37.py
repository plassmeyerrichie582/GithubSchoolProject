import requests
from bs4 import BeautifulSoup

def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to retrieve the page")
        return None

url = "http://example.com"
html_content = get_html(url)

if html_content is not None:
    soup = BeautifulSoup(html_content, 'lxml')
    # Add your code here using the parsed HTML content
else:
    print(f"Failed to load {url}")
