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
data = json.loads(json_str)

print(type(data))