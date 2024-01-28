from random import randint

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# initialize game:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# given:
max_tries = 3
start_number  = 1
end_number = 10

machine_number = randint(start_number, end_number)
print("I'm thinking about a number, between [{}, {}]. Can you guess it in {} tries?".
    format(start_number, end_number, max_tries))
# flag to trace weather the user has guessed
guessed = False

# for debugging:
# print("machine_number = ", machine_number)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# game play logic
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
for try_count in range( max_tries ):
    # get user number - loop until a number in the given interval is entered:
    while True:
        user_number = int(input("\nTry {}. Enter a number: ".format(try_count+1)))
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


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# check if user have guessed or max tries have been reached and print result:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
print("~" * 60)
if guessed:
    print(f"You win !!! {machine_number} was my number! And you've guessed it in {try_count+1} tries!") # type:ignore
else:
    print("You lose! My number was {}".format(machine_number))
print("~" * 60)