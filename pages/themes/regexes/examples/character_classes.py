import re

# # match bg mobile phone numbers
# matched = re.findall('\+3598[7-9]\d{7}', '+359888123456');
# print(matched)
# #OUTPUT: ['+359888123456']


# strings = ['petrov42','42petrov','ivan_pterov']
# rx = re.compile('[a-z]\w+')

# for string in strings:
#   matched = rx.search(string);
#   print("{} matched in {}".format(matched.group(),string) )

string = """line1
line2
line3 line4"""

matched = re.findall('line\d\s', string);
print(matched)