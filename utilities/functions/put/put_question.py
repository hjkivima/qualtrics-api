import requests
import importlib
import re
from config import questions
from dotenv import load_dotenv
import os

load_dotenv()

survey_id = os.environ.get("SURVEY_ID")


def create_data(question_name):
    question_data = questions[question_name]
    paths = dict(
        html_path=f"questions/{question_name}/index.html",
        js_path=f"questions/{question_name}/script.js",
        label_left_path=f"questions/{question_name}/label_left.html",
        label_right_path=f"questions/{question_name}/label_right.html",
    )

    for key in paths:
        if key in question_data:
            paths[key] = f"questions/{question_data[key]}"

    def read_file(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read()
        except:
            return ""

    def replace_placeholder(match, options):
        key = match.group(1)
        return options.get(key, f"[[{key}]]")

    html = read_file(paths["html_path"])

    html = re.sub(
        r"\[\[(.*?)\]\]",
        lambda match: replace_placeholder(match, question_data["html_substitutions"]),
        html,
    )

    javascript = read_file(paths["js_path"])

    javascript = re.sub(
        r"\[\[(.*?)\]\]",
        lambda match: replace_placeholder(match, question_data["js_substitutions"]),
        javascript,
    )

    label_left = read_file(paths["label_left_path"])
    label_right = read_file(paths["label_right_path"])

    return dict(
        html=html,
        javascript=javascript,
        label_left=label_left,
        label_right=label_right,
    )


def put_question(question_name, headers):
    question_data = questions[question_name]

    question_id = question_data["id"]

    data_dict = create_data(question_name)
    html = data_dict["html"]
    javascript = data_dict["javascript"]
    label_left = data_dict["label_left"]
    label_right = data_dict["label_right"]

    path = f"questions.{question_name}.question"

    if "question_path" in question_data:
        path = f"questions.{question_data['question_path']}.question"

    module = importlib.import_module(path)
    data = module.create_question(
        html, javascript, label_left, label_right, question_name
    )

    url = f"https://ca1.qualtrics.com/API/v3/survey-definitions/{survey_id}/questions/{question_id}"

    response = requests.put(url, json=data, headers=headers)
    print(response.text)
