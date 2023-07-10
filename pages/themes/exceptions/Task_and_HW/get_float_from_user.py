def get_float_from_user(msg):
	"""
		Summary:
			Asks the user to enter a number and
			- if he/she entered no valid python's number value => print:
				"***Enter an number, please!" and ask again.
			- if any other error occurs => print:
				"***Oops, something went wrong! Try again!" and ask again

			Returns the user input, as float, when no errors occurred.

		Usage:
			user_number = get_float_from_user("the message to show to the user")

		Arguments:
			msg {[string]} - - [the message to show to the user]

		Returns:
			[float] - - [the number entered from user, converted to float]
	"""

	while True:
		try:
			number = float(input(msg))
		except ValueError:
			print("***Enter a number, please!")
		except:
			print("\n***Oops, something went wrong! Try again!\n")
		else:
			return number

user_height = get_float_from_user("I need to know your height in centimetres: ")
user_weight = get_float_from_user("And your weight in kilograms: ")
print("Your height is: {:5.2f}cm. and you weight {:.2f}kg.".format(user_height, user_weight))

# $ python3.6 get_number_from_user.py
# I need to know your height in centimetres: 192
# And your weight in kilograms: 98.60
# Your height is: 192.00cm. and you weight 98.60kg.