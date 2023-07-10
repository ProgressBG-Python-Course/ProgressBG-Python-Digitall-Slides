from random import randint

# given:
max_tries = 3
start_number  = 1
end_number = 10

# game init:
machine_number = randint(start_number, end_number)
print("""I'm thinking about a number, between [{}, {}].
    Can you guess it?""".format(start_number, end_number))
try_count = 1
# flag to trace weather the user has guessed
guessed = False

# for debugging:
# print("machine_number = ", machine_number)

# play
while try_count <= max_tries:
    # get user number - loop until a number in the given interval is entered:
    while True:
        user_number = int(input("Try {}. Enter a number: ".format(try_count)))
        if ( start_number <= user_number <= end_number):
            break
        else:
            print("Enter a number in [{}, {}]".format(start_number, end_number))

    # check against machine number:
    if user_number == machine_number:
        guessed = True
        break
    elif user_number < machine_number:
        print("Your guess is less than my number.")
    else:
        print("your guess is greater than my number.")

    # increment try counter
    try_count += 1


# check if user have guessed or max tries have been reached:
if guessed:
    print("You win !!!")
else:
    print("You lose! My number was ", machine_number)
