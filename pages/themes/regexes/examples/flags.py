import re

text = """123
ABC
456"""
rx = re.compile('(?is)123.abc')

res = rx.search(text)
if res:
  print(res.group(0))
else:
  print("No match!")