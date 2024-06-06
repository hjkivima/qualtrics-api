import requests
from pprint import pformat
import os
from config import questions
from dotenv import load_dotenv

load_dotenv()

survey_id = os.environ.get("SURVEY_ID")


def get_question(question_name, headers):
    question_id = questions[question_name]["id"]
    url = f"https://ca1.qualtrics.com/API/v3/survey-definitions/{survey_id}/questions/{question_id}"
    response = requests.get(url, headers=headers)
    response_data = response.json()
    result = response_data.get("result", {})
    print("get_question", question_name, response.status_code)
    directory = f"questions/{question_name}/download"
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(f"{directory}/question.py", "w") as f:
        f.write(f"question_data = {pformat(result)}")

    question_js = result.get("QuestionJS", "")
    if question_js:
        with open(f"{directory}/script.js", "w") as js_file:
            js_file.write(question_js)

    question_html = result.get("QuestionText", "")
    if question_html:
        with open(f"{directory}/index.html", "w") as html_file:
            html_file.write(question_html)
