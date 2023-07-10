string = "АБВ 123 ИЙК ЩЮЯ"

# open a file handler for writing in binary mode"
with open("encoded_cp1251.txt", "w+b") as fh:
  bytes_sequence = string.encode(encoding="cp1251")
  print(bytes_sequence)

  fh.write(bytes_sequence)

# now re-open the file: encoded_cp1251.txt with encoding cp1251(windows-1251)