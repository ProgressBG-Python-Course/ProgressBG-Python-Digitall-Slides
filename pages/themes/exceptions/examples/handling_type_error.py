def div(x,y):
	return x/y

try:
	user_number = int(input("Enter a number: "))
	res = div(10,x)
	print("Result is {}".format(res))
except ValueError:
	print("You did not enter a number!")
except ZeroDivisionError:
	print("Enter a number different from zero (0)!")
except:
	print("Oops! Something went wrong!")

