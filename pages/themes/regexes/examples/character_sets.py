import re

# # match any one of the vocals
# matched = re.findall(r'[aeiouy]','astroid' );
# print(matched)
# #OUTPUT: ['a', 'o', 'i']

# # match any consecutive vocals - one or more times
# matched = re.findall(r'[aeiouy]+','astroid' );
# print(matched)
# #OUTPUT: ['a', 'oi']

# # match bg mobile phone numbers
# matched = re.findall('\+3598[7-9][0-9]{7}', '+359888123456');
# print(matched)
# #OUTPUT: ['+359888123456']

# matched = re.findall('[1-5-]', '12-34');
# print(matched)
# #OUTPUT: ['1', '2', '-', '3', '4']

# match any non-vocal:
matched = re.findall(r'[^aeiouy]','astroid' );
print(matched)
