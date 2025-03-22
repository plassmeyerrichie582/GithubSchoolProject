import requests
import os

def send_email(subject, body):
    url = "https://accounts.dymo.com/verify"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }
    
    payload = f"js=1&email={os.getenv('DEMO_USER')}&password={os.getenv('DEMO_PASSWORD')}"
    
    response = requests.post(url, data=payload, headers=headers)
    
    if response.status_code == 204:
        print("Email sent successfully!")
    else:
        print(f"Failed to send email. Status code: {response.status_code}")

if __name__ == "__main__":
    subject = "Welcome to Dymo"
    body = """
    Dear User,
    Welcome to Dymo! This is a test email using Dymo's API.
    """
    
    send_email(subject, body)
