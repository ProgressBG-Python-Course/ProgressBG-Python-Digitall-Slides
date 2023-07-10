import re

def example1():
  strings = [
    '',
    'a',
    '@',
    '@a',
    'aa',
    'a!',
    'a,a',
  ]
  rx = re.compile(r'\b');

  for string in strings:
    res = rx.findall(string)
    print("{} word bounders counted in {}".format(len(res), string))

def example2():
  strings = [
    'ana',
    'ana bel',
  ]
  rx = re.compile(r'^a\w+a$');

  for string in strings:
    res = rx.findall(string)
    print("{} matches in {}".format(len(res), string))



example2()