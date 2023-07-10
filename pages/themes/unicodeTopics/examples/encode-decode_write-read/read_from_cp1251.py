win1251file = "write_to_cp1251.txt"

# open a file handler for reading in text mode, with encoding="cp1251""
with open(win1251file, "r", encoding="cp1251") as f:
    print(f.read())