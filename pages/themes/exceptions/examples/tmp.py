class MyError(Exception):
	pass


try:
  x = 2
  res = 10/x
  print("Result is {}".format(res))
except TypeError:
  print("You did not enter a number!")
except ZeroDivisionError:
  print("Enter a number different from zero (0)!")
except:
  print("Oops! Something went wrong!")