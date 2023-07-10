try:
	# code, which can raise an exception
	user_number = int(input("Enter a number: "))
except Exception as e:
	# do something if an Exception was raised
	print("You did not enter a number!")
else:
	# do something if there was no Exception
	print("Your number is ", user_number)
finally:
	# do something no matter if an Exception was raised or not
	print("That was all!")

# Enter a number: iva
# You did not enter a number!
# That was all!
