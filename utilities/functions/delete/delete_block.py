import requests
import utilities.get_headers as get_headers


def delete_block(survey_id, block_id):
    headers = get_headers.get_headers(requests)
    url = f"https://ca1.qualtrics.com/API/v3/survey-definitions/{survey_id}/blocks/{block_id}"
    response = requests.delete(url, headers=headers)
    with open("JSON/message.json", "w") as f:
        f.write(response.text)
