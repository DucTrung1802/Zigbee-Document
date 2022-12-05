payload = "05 00 c6 46 00 f0 e8 e8 00 00 c6 46 78 f0 e8 e8 00 00 c6 46 f0 f0 e8 e8 00 00 c6 46 3d f0 e8 e8 00 00 c6 46 ae f0 e8 e8 00 00 c6 c6 13 f0 e8 e8 00 00"

sliced_payload = payload.split(" ")

for item in sliced_payload:
    if hex(int(item, 16)) == "0x0":
        print("0x00", end=", ")
    else:
        print(hex(int(item, 16)), end=", ")
