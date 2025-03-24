import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")
        return soup
    else:
        print(f"Failed to retrieve the HTML. Status code: {response.status_code}")
        return None

def main():
    url = "https://www.example.com"
    soup = fetch_html(url)
    if soup:
        # Code here
        pass

if __name__ == "__main__":
    main()
