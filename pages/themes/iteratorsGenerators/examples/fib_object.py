class FibsIterable:
  def __init__(self, limit):
    self.a = 0
    self.b = 1
    self.limit = limit
  def __next__(self):
    self.a, self.b = self.b, self.a + self.b
    if ( self.a < self.limit):
      return self.a
    else:
      raise StopIteration
  def __iter__(self):
    return self

fib_numbers = FibsIterable(30)

for i in fib_numbers:
  print( i )