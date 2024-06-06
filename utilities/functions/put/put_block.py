import requests
import importlib
from config import blocks
from dotenv import load_dotenv
import os

load_dotenv()

survey_id = os.environ.get("SURVEY_ID")


def block_data(block_elements, block_id, block_text, loop_and_merge):
    return {
        "BlockElements": block_elements,
        "Description": block_text,
        "ID": block_id,
        "Options": {
            "BlockLocking": "false",
            "BlockVisibility": "Expanded",
            "Looping": "Static",
            "LoopingOptions": {
                "Randomization": "All",
                "Static": loop_and_merge,
            },
            "RandomizeQuestions": "false",
        },
        "SubType": "",
        "Type": "Standard",
    }


def put_block(question_name, headers):

    block_id = blocks[question_name]["id"]
    block_elements = blocks[question_name]["elements"]
    block_title = blocks[question_name]["title"]
    loop_and_merge_path = blocks[question_name]["loop_and_merge_path"]

    module = importlib.import_module(loop_and_merge_path)

    loop_and_merge = module.loop_and_merge

    data = block_data(block_elements, block_id, block_title, loop_and_merge)

    url = f"https://ca1.qualtrics.com/API/v3/survey-definitions/{survey_id}/blocks/{block_id}"

    response = requests.put(url, json=data, headers=headers)
    print("put_block", question_name, response.status_code)
