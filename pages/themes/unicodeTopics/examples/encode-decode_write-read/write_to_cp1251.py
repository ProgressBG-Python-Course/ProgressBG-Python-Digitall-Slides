string = "АБВ 123 ИЙК ЩЮЯ"

# open a file for writing in text mode, with encoding="cp1251" "
with open("write_to_cp1251.txt", "w+", encoding="cp1251") as fh:
  fh.write(string)

# now re-open the file: write_to_cp1251.txt with encoding cp1251(windows-1251)