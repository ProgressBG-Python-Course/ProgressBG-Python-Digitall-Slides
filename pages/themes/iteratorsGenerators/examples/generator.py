nested = [[1, 2], [3, 4], [5]]

def flatten(nested):
  for sublist in nested:
    for element in sublist:
      yield element


g = flatten(nested)
print( next(g) )
print( next(g) )
print( next(g) )
print( next(g) )