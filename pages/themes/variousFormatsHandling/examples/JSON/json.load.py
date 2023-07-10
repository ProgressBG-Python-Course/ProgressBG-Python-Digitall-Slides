import json
from operator import itemgetter

json_file = "sample.json"

#read json from file
with open(json_file) as f:
    json_data = json.load(f)

# print the list sorted by "price" 
for i in sorted(json_data,key=itemgetter("price")):
	print(i)