try:
	user_number = int(input("Enter a number: "))
	res = 10/user_number
except ValueError:
	print("You did not enter a number!")
except ZeroDivisionError:
	print("Enter a number different from zero (0)!")
