import json
from operator import itemgetter

json_str = """ 
	[
	    {
	        "name": "apple",
	        "price": 1.80
	    },
	    {
	        "name": "orange",
	        "price": 2.10
	    },
	    {
	        "name": "bananas",
	        "price": 1.60
	    }
	]
"""


#read json from string
json_data = json.loads(json_str)

# print the list sorted by "price" 
for i in sorted(json_data,key=itemgetter("price")):
	print(i)