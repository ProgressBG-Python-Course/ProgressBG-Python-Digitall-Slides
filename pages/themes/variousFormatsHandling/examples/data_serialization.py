import pickle

# let's serialize a simple dict
prices = { 'apples': 2.50, 'oranges': 1.90, 'bananas': 2.40 }

print("convert an object to a serialized string")
serialized_prices = pickle.dumps( prices )
print(serialized_prices)

print("de-serialize (unpickle) an object")
received_prices = pickle.loads( serialized_prices )
print(received_prices)