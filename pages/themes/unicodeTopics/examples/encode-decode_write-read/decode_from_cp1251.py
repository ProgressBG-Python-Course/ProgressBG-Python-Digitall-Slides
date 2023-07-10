win1251file = "encode_to_cp1251.txt"

# open a file handler for reading in binary mode"
with open(win1251file, "r+b") as f:
    bytestring = f.read()

    decoded_string = bytestring.decode(encoding="cp1251")
    print(decoded_string)