### create empty tuple:
empty = ()
print( empty )
# ()

### create tuple with one element - note the trailing comma!
t = (99,)
print(t)
# (99,)

### create tuple of 3 elements:
point3d = (4, 0, 3)
print(point3d)
# (4, 0, 3)

### retrieve element feom a tuple
x = point3d[0]
print(x)
# 4

### attempt to change element in a tuple
# point3d[0] = 99
# TypeError: 'tuple' object does not support item assignment
