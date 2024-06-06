import requests
from pprint import pformat
from config import blocks
import os
from dotenv import load_dotenv

load_dotenv()

survey_id = os.environ.get("SURVEY_ID")


def get_block(question_name, headers):
    block_id = blocks[question_name]["id"]

    url = f"https://ca1.qualtrics.com/API/v3/survey-definitions/{survey_id}/blocks/{block_id}"
    response = requests.get(url, headers=headers)
    response_data = response.json()
    result = response_data.get("result", {})
    print("get_block", question_name, response.status_code)

    directory = f"./blocks/{question_name}"
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(f"{directory}/block.py", "w") as f:
        f.write(f"block_data = {pformat(result)}")
