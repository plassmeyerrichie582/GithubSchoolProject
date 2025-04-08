import requests
import os

def download_and_extract_file(url, destination):
    response = requests.get(url)
    if response.status_code == 200:
        with open(destination, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded and saved at {destination}")
    else:
        print("Failed to download the file.")

def main():
    url = "https://raw.githubusercontent.com/programmingchallenge/astronomy-tutorial/master/data.csv"
    destination = os.path.join("/Users/someuser/Desktop", "astronomy_tutorial_data")
    download_and_extract_file(url, destination)

if __name__ == "__main__":
    main()
