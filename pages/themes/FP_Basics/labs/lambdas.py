from functools import reduce


l = [1,2,3,4,5]



output = reduce( lambda i,j: i+j, l)

print( output )