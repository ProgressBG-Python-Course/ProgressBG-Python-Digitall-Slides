from random import randint

# given:
max_tries = 5
start_number  = 1
end_number = 100

# game start:
machine_number = randint(start_number, end_number)
print("machine_number = ", machine_number)
print("I'm thinking about a number, between [{}, {}]. Can you guess it?".format(
    start_number, end_number))
try_count = 0

# play
while True:
    try_count += 1

    if try_count == max_tries:
        print("You lose! My number was ", machine_number)
        break    

    # get user guess:
    while True:
        user_number = int(input("Try {}.Enter a number: ".format(try_count)))
        if (user_number <=end_number and user_number >=start_number):
            break
    
    # check against machine number:
    if user_number == machine_number:
        print("*** You Win!!! ***")
        break
    elif user_number < machine_number:
        print("Your guess is less than my number. Try again")
    else:
        print("your guess is greater than my number. Try again!")



