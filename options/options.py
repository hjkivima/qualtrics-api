def create_options_data():
    css_file_path = f"options/style.css"

    with open(css_file_path, "r", encoding="utf-8") as file:
        css_string = file.read()

    return {
        "BackButton": False,
        "BallotBoxStuffingPrevention": False,
        "CustomStyles": {"customCSS": css_string},
        "Header": "",
        "Footer": "",
        "NoIndex": "Yes",
        "NextButton": "←",
        "PartialData": "+1 week",
        "PreviousButton": "←",
        "ProgressBarDisplay": "None",
        "SaveAndContinue": True,
        "SecureResponseFiles": "true",
        "SurveyExpiration": "on",
        "SurveyProtection": "PublicSurvey",
        "SurveyTermination": "DefaultMessage",
        "ValidationMessage": "MS_abcdefg12345",
        "SkinLibrary": "umich",
        "SkinType": "templated",
        "Skin": {
            "brandingId": None,
            "templateId": "*2014",
            "overrides": {
                "answerText": {"size": "20px"},
                "questionText": {"size": "22px"},
            },
        },
    }


options_data = create_options_data()
