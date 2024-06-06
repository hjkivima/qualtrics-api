from utilities.create_embedded_data_dictionary import create_embedded_data_dictionary
from itertools import product


def create_embedded_data(array, fl_number):
    return {
        "Type": "EmbeddedData",
        "FlowID": f"FL_{fl_number}",
        "EmbeddedData": array,
    }


def create_combinations(*arrays, fl_number=100):
    treatment = 1
    combinations_list = []

    for combination in product(*arrays):

        emb_data = []
        for item in combination:

            for key, value in item.items():
                emb_data.append(create_embedded_data_dictionary(key, value))
        emb_data.append(create_embedded_data_dictionary("treatment", str(treatment)))
        treatment = treatment + 1
        combinations_list.append(create_embedded_data(emb_data, fl_number))
        fl_number = fl_number + 1
    return combinations_list


male_string = "${e://Field/maleName}"
man_string = "${e://Field/manName}"

female_string = "${e://Field/femaleName}"
woman_string = "${e://Field/womanName}"

randomized_embedded_data = create_combinations(
    [
        {
            "leftGender": woman_string,
            "rightGender": man_string,
        },
        {
            "leftGender": man_string,
            "rightGender": woman_string,
        },
    ],
    [
        {
            "topGender": female_string,
            "bottomGender": male_string,
        },
        {
            "topGender": male_string,
            "bottomGender": female_string,
        },
    ],
)
