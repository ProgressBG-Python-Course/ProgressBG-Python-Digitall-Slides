def get_string_from_user(msg):
	"""
		Summary:
			Asks the user to enter a string and
			- if any error occurs => print:
				"***Oops, something went wrong! Try again!" and ask again

			Returns the user input, as string, when no errors occurred.

		Usage:
			user_input = get_string_from_user("enter a user name: ")

		Arguments:
			msg {[string]} -- [the string to be displayed to the user,]

		Returns:
			[string] -- [the string entered from user]
	"""

	while True:
		try:
			user_input = input(msg)
		except:
			print("\n***Oops, something went wrong! Try again!\n")
		else:
			return user_input

user_name = get_string_from_user("Enter your name, please: ")
user_place = get_string_from_user("Where are you from?: ")
print("Hello {}! How is the weather in {} today?".format(user_name, user_place))
