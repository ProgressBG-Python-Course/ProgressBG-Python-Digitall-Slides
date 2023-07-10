import re

phone_numners = ['+359 88 7123 456', '+359 88 7123456' ]

regex = r'\+\d{3}\s\d{2}\s\d{4}\s\d{3}'

for number in phone_numners:
  if re.match(regex,number):
    print("{} is a valid number format".format(number))
  else:
    print("{} is NOT IN A VALID FORMAT".format(number))


# print( re.search(r'abc', "123abc123").group(0) )