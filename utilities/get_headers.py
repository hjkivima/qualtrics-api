from dotenv import load_dotenv
import os
import requests

load_dotenv()

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")


def get_headers():
    data_center_id = "ca1"
    base_url = f"https://{data_center_id}.qualtrics.com/oauth2/token"
    data = {"grant_type": "client_credentials", "scope": "manage:all"}

    r = requests.post(base_url, auth=(CLIENT_ID, CLIENT_SECRET), data=data)

    print("get_headers", r.status_code)
    api_token = r.json()["access_token"]

    return {
        "Content-Type": "application/json",
        "Accept": "application/json, application/xml",
        "Authorization": f"Bearer {api_token}",
    }
