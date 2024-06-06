import requests
from flow.flow import create_flow
from dotenv import load_dotenv
import os

load_dotenv()

survey_id = os.environ.get("SURVEY_ID")


def put_flow(headers):

    flow = create_flow()

    data = {
        "Flow": flow,
        "FlowID": "FL_1",
        "Type": "Root",
    }

    url = f"https://ca1.qualtrics.com/API/v3/survey-definitions/{survey_id}/flow"

    response = requests.put(url, json=data, headers=headers)
    print("put_flow", response.status_code)
