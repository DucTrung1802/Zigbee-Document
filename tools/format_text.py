text = "znp.waitFor(...Type.AREQ, Subsystem.ZDO, 'simpleDescRsp', ...)"


def toName(text):
    text = text.lower()
    text = text.replace(" ", "_")
    text = text + ".md"
    print(text)


toName(text)
