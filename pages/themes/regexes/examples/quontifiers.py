import re

def star_quantifier():
  string = 'ala bala'

  # greedy
  matched = re.findall(r'a.*a',string );
  print(matched)

  # non-greedy
  matched = re.findall(r'a.*?a',string );
  print(matched)

  #any character - non-gready
  matched = re.findall(r'.*',string );
  print(matched)

  #any character - non-gready
  matched = re.findall(r'.*?',string );
  print(matched)

def interval_quantifier():
  matched = re.findall(r'\d{2,4}','123456789' ) # gready
  print(matched)

  matched = re.findall(r'\d{2,4}?','123456789' ) # non-gready
  print(matched)

interval_quantifier()

# matched = "ala aa bala".match(/a.{3,}a/g);
# console.log(`matched: ${matched}`);
# # matched: ala aa bala

# matched = "ala aa bala".match(/a.{3,}?a/g);
# console.log(`matched: ${matched}`);
# # matched: ala a,a bala
