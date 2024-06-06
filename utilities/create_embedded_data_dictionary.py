def create_embedded_data_dictionary(name, value=None):
    base_dict = {
        "Description": name,
        "Type": "Custom" if value else "Recipient",
        "Field": name,
        "VariableType": "String",
        "DataVisibility": [],
        "AnalyzeText": False,
    }
    if value is not None:
        base_dict["Value"] = value
    return base_dict
