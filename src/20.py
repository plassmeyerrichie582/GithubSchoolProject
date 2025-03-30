import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.find('div', {'id': 'content'}).text.strip()
        return content
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

url = "https://example.com"
page_content = fetch_page(url)
if page_content is not None:
    print(page_content)
