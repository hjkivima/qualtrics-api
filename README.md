# Qualtrics App

Instructions

- You first need to create a `.env` file in the main directory. This file needs to contain three variables: `SURVEY_ID`, `CLIENT_ID` and `CLIENT_SECRET`.

  - You can find `SURVEY_ID` by going to the survey you want to edit in Qualtrics, and using the part of the URL string that starts with `SV_`

  - Read [here](https://api.qualtrics.com/24d63382c3a88-api-quick-start) on how to get the values of `CLIENT_ID` and `CLIENT_SECRET`

- Run the app using a command such as `python main.py` or `python3 main.py`

- In the `main.py` file, you can use the `get_` functions to download data. For example, `get_flow()` will download a file called `flow_download.py` in the main directory.

- Using the `get` functions will download parts of the survey. You can then edit the downloaded objects and send them back using the `put` functions
