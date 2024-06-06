import requests
import utilities.get_headers as get_headers
from dotenv import load_dotenv
import os

load_dotenv()

survey_id = os.environ.get("SURVEY_ID")


def get_options():
    headers = get_headers.get_headers(requests)
    url = f"https://ca1.qualtrics.com/API/v3/survey-definitions/{survey_id}/options"
    response = requests.get(url, headers=headers)
    print(response.text)
