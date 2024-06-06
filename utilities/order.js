let currentPageNumber = parseInt("${e://Field/currentPageNumber}");
currentPageNumber = currentPageNumber + 1;
Qualtrics.SurveyEngine.setEmbeddedData("currentPageNumber", currentPageNumber);

const loopRow = "${lm://Field/1}";
Qualtrics.SurveyEngine.setEmbeddedData("order_" + loopRow, currentPageNumber);
