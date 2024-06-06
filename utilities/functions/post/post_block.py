import requests
import utilities.get_headers as get_headers
import json


def post_block(survey_id, data):
    headers = get_headers.get_headers(requests)

    url = f"https://ca1.qualtrics.com/API/v3/survey-definitions/{survey_id}/blocks"

    response = requests.post(url, data=json.dumps(data), headers=headers)
    response_data = response.json()
    block_id = response_data.get("result", {}).get("BlockID", None)

    print(response.text)

    with open("JSON/message.json", "w") as f:
        f.write(response.text)

    return block_id
