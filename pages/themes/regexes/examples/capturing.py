import re

user = 'Ivan Ivanov: +359 887123456'

rx = re.compile("""(?x)
  ([A-Z]\w+)\s+   # capture first name
  ([A-Z]\w+):\s+  # capture sur name
  \+(\d{3})\s     # capture country code
  (\d{6,8})       # capture number
""")

res = rx.search(user)
if res:
  i = 0
  for t in res.groups():
    print("Capture {}: {}".format(i,t))
    i+=1