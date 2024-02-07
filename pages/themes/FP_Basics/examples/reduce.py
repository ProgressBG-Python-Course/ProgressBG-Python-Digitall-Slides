from functools import reduce

# *** sum the numbers from 0 to 10, including:
# res = reduce(lambda a,b: a+b, range(11))

# print(res)


# # reduce to price sum
# products = [
# 	{'name':'apples', 'price': 2},
# 	{'name':'oranges', 'price': 5},
# 	{'name':'bananas', 'price': 3},
# ]

# total_price = reduce(lambda price, product:price+product['price'], products, 0 )
# print(total_price)

# map-reduce: sum variable number of lists positionaly
l1 = [1,2,3]
l2 = [1,2,3]
l3 = [1,2,3]
l = map(lambda *t: reduce(lambda a,b: a+b, t) , l1, l2,l3)
print( list(l) )

