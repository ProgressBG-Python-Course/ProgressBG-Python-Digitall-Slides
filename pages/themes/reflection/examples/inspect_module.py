import inspect

def foo():
  func_name = inspect.stack()[0][3]
  caller_name = inspect.stack()[1][3]
  print("I'm {}.\n{} called me!".format(func_name,caller_name))

def bar(f):
  f()

bar(foo)

