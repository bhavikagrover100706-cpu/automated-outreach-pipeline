import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("PROSPEO_API_KEY")

headers = {
    "accept": "application/json",
    "X-KEY": api_key,
    "content-type": "application/json"
}


def get_contacts(company_domain):
    payload = {
        "page": 1,
        "filters": {
            "company": {
                "websites": {
                    "include": [
                        company_domain
                    ]
                }
            }
        }
    }

    response = requests.post(
        "https://api.prospeo.io/search-person",
        json=payload,
        headers=headers
    )

    if response.status_code == 200:
        data = response.json()
        return data.get("results", [])

    return []


def get_email(person_id):
    payload = {
        "data": {
            "person_id": person_id
        }
    }

    response = requests.post(
        "https://api.prospeo.io/enrich-person",
        json=payload,
        headers=headers
    )

    data = response.json()

    if "person" not in data:
        return None

    email_info = data["person"].get("email")

    if not email_info:
        return None

    if not email_info.get("revealed"):
        return None

    return email_info.get("email")