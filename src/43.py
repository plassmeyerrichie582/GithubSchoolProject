import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find('div', class_='content').text
    return content

# Replace the url with the actual URL of your data page
url = "https://example.com/data"
data = fetch_data(url)

# Extract specific data points if needed
selected_data = [50, 30, 40]

df = pd.DataFrame(data=[data] * len(selected_data), columns=['value'])
df['total'] = df['value'].apply(sum)
df_selected = df[selected_data]
print(df_selected)
