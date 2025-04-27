import requests
from bs4 import BeautifulSoup

def search_articles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("div", class_="article")
    
    for article in articles:
        title = article.find("h2").text
        link = article.find("a")["href"]
        
        print(f"Title: {title}")
        print(f"Link: {link}\n")

search_articles("https://www.example.com/education/")
