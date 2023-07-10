class SimplestNumbersIterator():
  """Simplest Number Iterator, which can iterate on only two values - 1 and 2.

    Disclaimer: Use it just to trace how __next__ and __iter__ operators works.
                      This example is not useful in real world!
  """
  def __init__(self):
    self.num = 0
    self.max = 2

  def __iter__(self):
    return self

  def __next__(self):
    # generate a number to return
    if self.num < self.max:
      self.num += 1
      print("Iterate on", self.num)
      return self.num
    else:
      raise StopIteration

def test_simplest_numbers_iterator(test):
  """To test the simplest_numbers_iterator, use:

      test_simplest_numbers_iterator("for")
        -- to see the iterator behaviour on for loop
      test_simplest_numbers_iterator("next")
        -- to see the iterator behaviour on next() call
  """
  print_header("Testing SimplestNumbersIterator on {}".format(test), "#", 50)
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


def print_header(msg, symbol, width):
  """Summary

  Args:
      msg (String): the text to be printed
      symbol (String): the border symbol
      width (Int): the width of printing area
  """
  print("\n")
  print(symbol*width)
  print(symbol+msg.center(width-2)+symbol)
  print(symbol*width)


test_simplest_numbers_iterator("for")
test_simplest_numbers_iterator("next")