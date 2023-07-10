def foo_generator():
  yield 1
  yield 2

foo_gen = foo_generator()

print( next(foo_gen) )
print( next(foo_gen) )
