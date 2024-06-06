def create_slider_question(
    html_path, javascript_path, label1_path, label2_path, data_export_tag
):

    for path in [html_path, javascript_path, label1_path, label2_path]:
        files = {}
        with open(path, "r") as f:
            files[path] = f.read()

    return {
        "ChoiceOrder": [1],
        "Choices": {"1": {"Display": ""}},
        "Configuration": {
            "CSSliderMax": 100,
            "CSSliderMin": 0,
            "CustomStart": True,
            "SliderStartPositions": {"1": 0.50},
            "GridLines": 10,
            "MobileFirst": True,
            "NotApplicable": False,
            "NumDecimals": "0",
            "QuestionDescriptionOption": "UseText",
            "ShowValue": True,
            "SnapToGrid": False,
        },
        "DataExportTag": data_export_tag,
        "DataVisibility": {"Hidden": False, "Private": False},
        "DefaultChoices": False,
        "Labels": {
            "1": {"Display": files["label1_path"]},
            "2": {"Display": files["label2_path"]},
        },
        "NextAnswerId": 1,
        "NextChoiceId": 2,
        "QuestionJS": files["javascript_path"],
        "QuestionText": files["html_path"],
        "QuestionType": "Slider",
        "Selector": "HSLIDER",
        "Validation": {
            "Settings": {
                "ForceResponse": "ON",
                "ForceResponseType": "ON",
                "Type": "None",
            }
        },
    }
