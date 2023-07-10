import re

strings = [
  'Icecream with strawberries?',
  'Icecream with blueberries?',
  'Icecream with raspberries?',
  'Icecream with strawraspberries?',
  'Icecream with berries?',
]
rx = re.compile(r'\b(?:straw|rasp)?berries');

for string in strings:
  res = rx.search(string)
  if res:
    print('{} YES!'.format(string))
  else:
    print('{} NO!'.format(string))
