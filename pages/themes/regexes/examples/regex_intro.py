import re

# the string to search with regex:
user_email = "prefix@domain.com"

# the regex to find if the userEmail contains '@' symbol:
regex = re.compile(r'@')

# do the match test:
if regex.search(user_email):
  print("Match!")
else:
  print("No match!")