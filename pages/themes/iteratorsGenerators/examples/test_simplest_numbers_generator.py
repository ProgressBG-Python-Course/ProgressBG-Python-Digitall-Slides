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

def test_simplest_numbers_generator(test):
  """To test the simplest_numbers_generator, use:

      test_simplest_numbers_generator("for")
        -- to see the generator behaviour on for loop
      test_simplest_numbers_generator("next")
        -- to see the generator behaviour on next() call
  """
  print_header("Testing simplest_numbers_generator on {}".format(test), "#", 50)

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


test_simplest_numbers_generator("for")
test_simplest_numbers_generator("next")
