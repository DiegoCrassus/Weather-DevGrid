class Messages:
    class ERROR:
        GENERIC = "Oops... We don't know what happened, but we're working to fix it. Please try again later."
        NOT_TREATMENT = "Something unexpected happened, and for your comfort, we will look into it."
        NOT_FOUND = "Oops... I believe the server is down."
        NONE = "I forgot to handle the null value and caused a problem for you."
        EXCEPTION = "Not handled."
        BUSINESS = "Exception: business rule error and something unexpected occurred."
        DIVISION = "Exception: error dividing by zero."
        FAIL_DATA_ACQUISITION = "Exception: failed to get data, the data came back empty. Verify if everything is okay with your request."

    class SUCCESS:
        DONE = "Success: Done."

    REQUEST_RECEIVED = "Request received."