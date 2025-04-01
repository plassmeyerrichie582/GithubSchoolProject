import requests

def fetch_news headlines():
    url = "https://newsapi.org/v2/top-headlines"
    response = requests.get(url)
    data = response.json()
    
    # Get headlines from news API
    headlines = data['articles']
    return headlines
    
fetch_news(headlines)
