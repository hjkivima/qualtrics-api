import requests
import utilities.get_headers as get_headers
import json
from dotenv import load_dotenv
import os
from options.options import create_options_data

load_dotenv()

survey_id = os.environ.get("SURVEY_ID")


def put_options(headers):
    data = create_options_data()

    url = f"https://ca1.qualtrics.com/API/v3/survey-definitions/{survey_id}/options"

    response = requests.put(url, data=json.dumps(data), headers=headers)
    print("put_options", response.status_code)
