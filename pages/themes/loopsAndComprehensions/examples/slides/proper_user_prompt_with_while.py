while True:
    user_number = int(input("Enter a positive number: "))
    if user_number > 0:
        break   

print("Nice, your number is: ", user_number)


user_number = int(input("Enter a positive number: "))
while user_number <= 0:
    user_number = int(input("Enter a positive number: "))   

print("Nice, your number is: ", user_number)
