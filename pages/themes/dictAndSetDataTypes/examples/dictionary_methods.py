prices = {
    "apples": 2.50,
    "oranges": 2.43,
    "bananas": 3.50
}

'''get all dictionary keys:'''
fruits = prices.keys()
print(fruits)
# dict_keys(['apples', 'oranges', 'bananas'])

prices_keys = prices.keys()
print("keys view before change:", prices_keys)

# add new key-value pair:
prices["new_key"]="new value"

print("keys view after the change:", prices_keys)




# price_list = prices.values()
# print(price_list)
# # dict_values([2.5, 2.43, 3.5])

# for key in prices:
#     print("{} - {}".format(key, prices[key]))
# # apples - 2.5
# # oranges - 2.43
# # bananas - 3.5

# for fruit, price in prices.items():
#     print("{} - {}".format(fruit, price))
