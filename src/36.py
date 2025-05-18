import requests
import os
from bs4 import BeautifulSoup

def fetch_text(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.find('p').get_text()
        return text
    else:
        print("Failed to retrieve the page")
        return None

# Example usage
url = "https://example.com"
text = fetch_text(url)
if text:
    print(text)
