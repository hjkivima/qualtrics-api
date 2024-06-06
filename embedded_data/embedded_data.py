from utilities.create_embedded_data_dictionary import create_embedded_data_dictionary
from itertools import product

costVariables = [
    create_embedded_data_dictionary("showup", "2"),
    create_embedded_data_dictionary("time", "10"),
    create_embedded_data_dictionary("bonus", "1"),
]

prolificVariables = [
    create_embedded_data_dictionary("PROLIFIC_PID"),
    create_embedded_data_dictionary("SESSION_ID"),
    create_embedded_data_dictionary("STUDY_ID"),
]

scoreVariables = [
    create_embedded_data_dictionary("maxScore", "20"),
    create_embedded_data_dictionary("score1", "5"),
    create_embedded_data_dictionary("score1Minus", "4"),
    create_embedded_data_dictionary("score1Plus", "6"),
    create_embedded_data_dictionary("score2", "10"),
    create_embedded_data_dictionary("score2Minus", "9"),
    create_embedded_data_dictionary("score2Plus", "11"),
    create_embedded_data_dictionary("score3", "15"),
    create_embedded_data_dictionary("score3Minus", "14"),
    create_embedded_data_dictionary("score3Plus", "16"),
]

genderVariables = [
    create_embedded_data_dictionary("maleName", "male"),
    create_embedded_data_dictionary("femaleName", "female"),
    create_embedded_data_dictionary("manName", "man"),
    create_embedded_data_dictionary("womanName", "woman"),
]

orderVariables = [
    create_embedded_data_dictionary("currentPageNumber", "0"),
]

modalHasBeenClickedVariables = [
    create_embedded_data_dictionary(f"modalHasBeenClicked_instructions", "0")
]


number_of_loop_rows_main = 5
number_of_loop_rows_followup = 7


for i in range(1, number_of_loop_rows_main + 1):
    orderVariables.append(
        create_embedded_data_dictionary(f"order_main_{i}"),
    )
    modalHasBeenClickedVariables.append(
        create_embedded_data_dictionary(f"modalHasBeenClicked_{i}", "0"),
    )


for i in range(1, number_of_loop_rows_followup + 1):
    orderVariables.append(
        create_embedded_data_dictionary(f"order_followup_{i}"),
    )
