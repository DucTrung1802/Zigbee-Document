text = "Add coordinator to the database if it is not there yet"


def toName(text):
    text = text.lower()
    text = text.replace(" ", "_")
    text = text + ".md"
    print(text)


toName(text)
