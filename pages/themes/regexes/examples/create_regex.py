import re

text = "ABRACADABRA"

regex = re.compile(r'aca', re.I)

if regex.search(text):
  print('Match')