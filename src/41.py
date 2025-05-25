import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        return html_content
    else:
        raise Exception(f"Failed to get HTML content. Status code: {response.status_code}")

def parse_html(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    # Add your parsing logic here

if __name__ == "__main__":
    url = "https://www.example.com"
    html_content = fetch_html(url)
    parse_html(html_content)
