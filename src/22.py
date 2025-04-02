import requests
import os

url = "https://www.example.com/your-file.txt"
response = requests.get(url)

if response.status_code == 200:
    with open(os.path.join("data", "file.txt"), "w") as file:
        file.write(response.text)
else:
    print(f"Failed to download file: {url}")
