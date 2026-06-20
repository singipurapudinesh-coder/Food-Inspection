def analyze_temperature(

prompt

):

    text = prompt.lower()


    if (

    "high temperature" in text

    or

    "very hot" in text

    ):

        return (

        "High Risk",

        "Avoid consuming spicy foods at very high temperatures."

        )


    if (

    "cold" in text

    ):

        return (

        "Low Risk",

        "Safe if food is stored properly."

        )


    return (

    "Moderate Risk",

    "Consume at normal serving temperature."

    )