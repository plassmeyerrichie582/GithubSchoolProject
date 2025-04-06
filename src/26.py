import requests
from bs4 import BeautifulSoup
import re

def get_random_code():
    # Example URL: "https://example.com"
    url = "https://example.com"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        code = soup.find('pre').get_text().strip()
        return code
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    random_code = get_random_code()
    if random_code:
        print(random_code)
