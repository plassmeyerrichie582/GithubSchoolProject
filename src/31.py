import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup.prettify())
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

url = "https://www.example.com"
fetch_page(url)
