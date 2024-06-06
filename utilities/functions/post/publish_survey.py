import requests
from dotenv import load_dotenv
import os

load_dotenv()

survey_id = os.environ.get("SURVEY_ID")


def publish_survey(headers):

    url = f"https://ca1.qualtrics.com/API/v3/survey-definitions/{survey_id}/versions"
    data = {"Description": "A published version", "Published": True}

    response = requests.post(url, json=data, headers=headers)

    print("publish_survey", response.status_code)
