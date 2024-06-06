import requests
import utilities.get_headers as get_headers


def create_survey(survey_name):
    headers = get_headers.get_headers(requests)
    url = "https://ca1.qualtrics.com/API/v3/survey-definitions"
    data = {
        "SurveyName": survey_name,
        "Language": "EN",
        "ProjectCategory": "CORE",
    }

    response = requests.post(url, json=data, headers=headers)

    response_data = response.json()
    survey_id = response_data.get("result", {}).get("SurveyID", None)
    default_block_id = response_data.get("result", {}).get("DefaultBlockID", None)

    print(response.text)

    return survey_id, default_block_id
