import requests
from bs4 import BeautifulSoup

def fetch_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.find_all('div', class_='content')
    else:
        return None

url = "https://example.com"
contents = fetch_content(url)
for content in contents:
    print(content.get_text())
