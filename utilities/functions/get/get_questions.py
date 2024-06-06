import requests
import utilities.get_headers as get_headers


def get_questions(survey_id):
    headers = get_headers.get_headers(requests)
    url = f"https://ca1.qualtrics.com/API/v3/survey-definitions/{survey_id}/questions"

    response = requests.get(url, headers=headers)

    with open("JSON/questions.json", "w") as f:
        f.write(response.text)
