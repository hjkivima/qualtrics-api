import requests

from pprint import pformat

from dotenv import load_dotenv
import os

load_dotenv()

survey_id = os.environ.get("SURVEY_ID")


def get_flow(headers):

    url = f"https://ca1.qualtrics.com/API/v3/survey-definitions/{survey_id}/flow"

    response = requests.get(url, headers=headers)
    # print(response.text)
    response_data = response.json()
    print("get_flow", response.status_code)
    result = response_data.get("result", {})  # .get("Flow", {})

    with open("./flow/flow_download.py", "w") as f:
        f.write(f"data = {pformat(result)}")
