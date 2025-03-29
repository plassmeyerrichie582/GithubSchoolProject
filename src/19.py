import requests
from bs4 import BeautifulSoup

def get_articles():
    url = "https://www.example.com/articles"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    articles = []
    for article in soup.find_all('div', class_='article'):
        title = article.find('h2').text
        link = article.find('a')['href']
        content = article.find('div', class_='content').text
        articles.append((title, link, content))
    
    return articles

articles = get_articles()
for title, link, content in articles:
    print(f"Title: {title}, Link: {link}, Content: {content}")
