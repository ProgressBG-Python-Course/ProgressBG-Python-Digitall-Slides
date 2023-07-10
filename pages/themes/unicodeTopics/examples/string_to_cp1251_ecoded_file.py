string = "АБВ 123 ИЙК ЩЮЯ"

# open a file handler for writing in binary mode"
with open("decoded_cp1251.txt", "w+b") as fh:
  bytes_decoded = string.encode(encoding="cp1251")
  print(bytes_decoded)

  fh.write(bytes_decoded)

# now open the file: decoded_cp1251.txt with encoding cp1251(windows-1251)

