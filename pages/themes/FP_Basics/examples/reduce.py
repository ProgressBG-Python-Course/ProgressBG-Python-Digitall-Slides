from functools import reduce

# *** sum the numbers from 0 to 10, including:
# res = reduce(lambda a,b: a+b, range(11))

# print(res)


# map-reduce: sum variable number of lists positionaly
l1 = [1,2,3]
l2 = [1,2,3]
l3 = [1,2,3]
l = map(lambda *t: reduce(lambda a,b: a+b, t) , l1, l2,l3)
print( list(l) )