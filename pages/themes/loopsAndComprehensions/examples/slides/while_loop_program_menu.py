# print program menu:
print("Select an action:")
print("1. Action 1")
print("2. Action 3")
print("3. Action 3")

while True:
	user_choice = int(input("Enter a number [0-4]: "))

	if user_choice == 1:
		print("Actin 1 fired!")
		break
	elif user_choice == 2:
		print("Actin 2 fired!")
		break
	elif user_choice == 3:
		print("Actin 3 fired!")
		break
	else:
		pass

