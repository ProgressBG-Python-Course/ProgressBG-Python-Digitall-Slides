import re

text = '\\stop'
re1 = '\\\\stop'
re2 = '\\stop'
re3 = r'\\stop'

print(len(r'\'))


if re.match(re1, text):
  print("re1 matched!")

if re.match(re2, text):
  print("re2 matched!")

if re.match(re3, text):
  print("re3 matched!")

