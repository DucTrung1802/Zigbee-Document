text = "Declare CLASS Znp of ZStackAdapter (ZNP = Zigbee Network Processor)"


def toName(text):
    text = text.lower()
    text = text.replace(" ", "_")
    text = text + ".md"
    print(text)


toName(text)
