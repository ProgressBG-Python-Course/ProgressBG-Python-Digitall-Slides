import json

mylist = [1,2,3]

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

prices = {
    "apples":2.50,
    "bananas":1.80,
    "strawberry": 3.20
}

print('List :', json.dumps(mylist))
print('Matrix :', json.dumps(matrix))
print('Prices :', json.dumps(prices,indent=4))