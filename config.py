questions = dict(instructions=dict(id="QID5"), top_gender=dict(id="QID1"))


blocks = dict(
    main=dict(
        id="BL_9TdlRLnyvlGLo7c",
        elements=[
            {"QuestionID": "QID14", "Type": "Question"},
            {"QuestionID": "QID7", "Type": "Question"},
            {"QuestionID": "QID1", "Type": "Question"},
            {"QuestionID": "QID6", "Type": "Question"},
        ],
        title="MAIN: LOOP AND MERGE",
        loop_and_merge_path="blocks.main.loop_and_merge",
    ),
    follow_up_questions=dict(
        id="BL_brMVqj4wkCzZeUm",
        elements=[
            {"QuestionID": "QID12", "Type": "Question"},
            {"QuestionID": "QID9", "Type": "Question"},
            {"QuestionID": "QID51", "Type": "Question"},
        ],
        title="FOLLOWUP QUESTIONS: LOOP AND MERGE",
        loop_and_merge_path="blocks.follow_up_questions.loop_and_merge",
    ),
)
