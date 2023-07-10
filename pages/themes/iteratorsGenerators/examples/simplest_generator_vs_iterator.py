def simplest_numbers_generator():
  """Simplest Number Generator, yielding only two values - 1 and 2.

    Disclaimer: Use it just to trace how next and yield operators works.
                This example is not useful in real world!
  """
  num = 1
  print("Yielding", num)
  yield num

  num +=1
  print("Yielding", num)
  yield 2

  num +=1
  print("Yielding", num)
  print("Sory, there is nothing to yield...")

class SimplestNumbersIterator():
  """Simplest Number Iterator, which can iterate on only two values - 1 and 2."""
  def __init__(self):
    self.num = 0
    self.max = 2

  def __iter__(self):
    return self

  def __next__(self):
    # generate a number to return
    if self.num < self.max:
      self.num += 1
      return self.num
    else:
      raise StopIteration


def test_simplest_numbers_generator(test):
  print("Testing simplest_numbers_generator on", test)

  # create num_gen generator
  num_gen = simplest_numbers_generator()
  # print( num_gen.__dir__() )

  if test == "for":
    for i in num_gen:
      print(i)
  elif test == "next":
    # ask the num_gen for 2 values:
    print( next(num_gen) )
    print( next(num_gen) )

    # ask num_gen for more values that it can yield
    print( next(num_gen) )

def test_simplest_numbers_iterator(test):
  print("Testing SimplestNumbersIterator on", test)
  num_iter = SimplestNumbersIterator()
  # print( num_iter.__dir__() )

  if test == "for":
    for i in num_iter:
      print(i)
  elif test == "next":
    print( next(num_iter) )
    print( next(num_iter) )
    print( next(num_iter) )
    print( next(num_iter) )
    print( next(num_iter) )


# test_simplest_numbers_iterator("for")
test_simplest_numbers_generator("for")
