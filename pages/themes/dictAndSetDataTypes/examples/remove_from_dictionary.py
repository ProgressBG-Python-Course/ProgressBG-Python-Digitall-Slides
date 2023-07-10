prices = {
    "apples": 2.50,
    "oranges": 2.43,
    "bananas": 3.50
}

'''remove 'apples' key:value pair from the dictinary, and return its value'''
apples_price = prices.pop('apples')
print(apples_price, prices)
# 2.5 {'oranges': 2.43, 'bananas': 3.5}

apples_price = prices.pop('apples', 5.00)
print(apples_price)
