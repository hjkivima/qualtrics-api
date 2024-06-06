import requests
import utilities.get_headers as get_headers
from pprint import pformat


def get_versions(
    survey_id,
):
    headers = get_headers.get_headers(requests)
    url = f"https://ca1.qualtrics.com/API/v3/survey-definitions/{survey_id}/versions"
    response = requests.get(url, headers=headers)
    response_data = response.json()
    print(response_data.get("meta", {}))
    result = response_data.get("result", {})

    with open("JSON/versions.py", "w") as f:
        f.write(f"data = {pformat(result)}")
