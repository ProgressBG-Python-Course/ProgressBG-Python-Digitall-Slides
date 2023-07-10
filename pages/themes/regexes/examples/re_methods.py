import re


def re_search():
  text = "123abc456"
  rx = re.compile('abc')

  res = rx.search(text,4)
  if res:
    print(res.group(0))
  else:
    print("No match!")

def re_match():
  text = "123abc456"
  rx = re.compile('abc')

  res = rx.match(text)

  if res:
    print(res.group(0))
  else:
    print("No match!")

def re_findall():
  text = "123abc456abcabc"
  rx = re.compile('\dabc')

  res = rx.findall(text)

  if res:
    print(res)
  else:
    print(res)

def match_object():
  text = "123abc456abc"
  rx = re.compile('(\d+)(abc)')

  res = rx.match(text)
  if res:
    print("res.group():", res.group()) #123abc
    print("res.groups():", res.groups()) #('123', 'abc')
  else:
    print("No match!")



match_object()
