import requests
import utilities.get_headers as get_headers
from pprint import pformat
from dotenv import load_dotenv
import os

load_dotenv()

survey_id = os.environ.get("SURVEY_ID")


def get_survey(headers):

    url = f"https://ca1.qualtrics.com/API/v3/survey-definitions/{survey_id}"

    response = requests.get(url, headers=headers)

    response_data = response.json()
    print("get_survey", response.status_code)
    result = response_data.get("result", {})

    with open(f"./survey.py", "w") as f:
        f.write(f"data = {pformat(result)}")
