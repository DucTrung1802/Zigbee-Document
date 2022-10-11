text = "Try this.znp.request(Subsystem.SYS, 'ping', ...) 3 times"


def toName(text):
    text = text.lower()
    text = text.replace(" ", "_")
    text = text + ".md"
    print(text)


toName(text)
