text = "this.znp.request(Subsystem.SYS, 'version', ...)"


def toName(text):
    text = text.lower()
    text = text.replace(" ", "_")
    text = text + ".md"
    print(text)


toName(text)
