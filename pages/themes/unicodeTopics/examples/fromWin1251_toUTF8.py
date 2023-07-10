input_file_name = "windows-1251_encoded_file.txt"
output_file_name = "utf8_encoded_file.txt"


def read_from(enc, file_name):
  # open file for read in textmode with encoding:
  with open(file_name,"r", encoding="cp1251") as f:
    decoded_content = f.read()

  return decoded_content

def write_to(enc, content, file_name):
  # open file for write in textmode with encoding:
   with open(file_name,"w+", encoding=enc) as f:
    f.write(content)


decoded_content = read_from("cp1251", input_file_name)
write_to("utf8", decoded_content, output_file_name)


