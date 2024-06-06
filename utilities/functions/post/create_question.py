import requests
import utilities.get_headers as get_headers


def create_question(survey_id, block_id, data):
    headers = get_headers.get_headers(requests)

    url = f"https://ca1.qualtrics.com/API/v3/survey-definitions/{survey_id}/questions?blockId={block_id}"

    response = requests.post(url, json=data, headers=headers)

    response_data = response.json()
    question_id = response_data.get("result", {}).get("QuestionID", None)

    print(response.text)

    with open("JSON/message.json", "w") as f:
        f.write(response.text)

    return question_id
