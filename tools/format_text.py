text = "znp.request(Subsystem.UTIL, 'getDeviceInfo', ...)"


def toName(text):
    text = text.lower()
    text = text.replace(" ", "_")
    text = text + ".md"
    print(text)


toName(text)
