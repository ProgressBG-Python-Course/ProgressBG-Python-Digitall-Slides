#!/usr/bin/env python3

import os.path
import sys

def usage():
    print("~"*50)
    print("USAGE:")
    print("cyr_to_utf8 <file_name>")
    print("~"*50)

def decode_from(enc, file_name):
  # open file for read in bytemode
  with open(file_name,"rb") as f:
    content_in_bytes = f.read()

  try:
      return content_in_bytes.decode(enc)
  except UnicodeDecodeError:
      print("Can not decode")
      raise


if __name__ == '__main__':
    try:
        input_file = sys.argv[1]
    except:
        usage()
        exit(0)

    input_file_name, extension = os.path.splitext(input_file)
    output_file = input_file_name+"_utf8_"+extension

    content = decode_from("cp1251",input_file)

    # write_in_UTF_file(content, output_file)
    with open(output_file, "w") as f:
      f.write(content)


