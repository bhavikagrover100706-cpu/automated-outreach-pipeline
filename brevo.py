import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("BREVO_API_KEY")

def send_email(email):
    headers = {
        "accept": "application/json",
        "api-key": api_key,
        "content-type": "application/json"

    }

    data = {
        "sender": {"name": "Your Name", "email": "bhavikagrover100706@gmail.com"} , 
        "to": [{"email": email}],
        "subject": "Hello from Brevo!",
        "htmlContent": "<html><body><h1>This is a test email from Brevo</h1></body></html>"
    }

    response = requests.post("https://api.brevo.com/v3/smtp/email", json=data, headers=headers)
    if response.status_code == 201:
        print(f"Email sent successfully to {email}")
    else:
        print(f"Failed to send email to {email}. Status code: {response.status_code}, Response: {response.text}")   