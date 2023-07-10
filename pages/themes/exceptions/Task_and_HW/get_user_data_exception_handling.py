def get_string_from_user(msg):
	while True:
		try:
			user_name = input(msg)
		except:
			print("\n***Oops, something went wrong! Try again!\n")
		else:
			return user_name

def get_number_from_user(msg):
	while True:
		try:
			number = int(input(msg))
		except ValueError:
			print("***Enter a number, please!")
		except:
			print("\n***Oops, something went wrong! Try again!\n")
		else:
			return number

user_data = {}
user_data["name"] = get_string_from_user("Enter your name, please: ")
user_data["height"] = get_number_from_user("I need to know your height in centimetres: ")
user_data["weight"] = get_number_from_user("And your weight in kilograms: ")

print(user_data)