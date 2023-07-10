import numpy

# lets create a python list
m = [
  [1,"a",3],
  [4,5,6],
  [7,8,9],
]

# and now create a numpy array from that list:
arr = numpy.array(m)

# now we can easily use numpy's multi-dim slicing:
print(arr[:,1])
print(type(arr[:,1]))
