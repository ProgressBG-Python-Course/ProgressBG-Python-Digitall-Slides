import re

text = "try to match: 2+3"
rx = re.compile('2\+3')

res = rx.search(text)
if res:
  print( res.group())