import json

prices = {
  "apples":2.50,
  "bananas":1.80,
  "strawberry": 3.20
}

with open('json_dump.out', 'w+') as fh:
  fh.write(json.dumps(prices, indent=2))
