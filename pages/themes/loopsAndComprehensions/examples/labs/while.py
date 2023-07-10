# TASK 1:
# ask the user to enter a number, until the number she enters is 5
if 0:
    userNumber = int(input("ENter a number: "))
    while userNumber != 5:
        userNumber = int(input("ENter a number: "))

# TASK 2:
if 0:
    # sum of even numbers in [1..100], which are divisible by 3;
    number = 1
    sum = 0

    while number<=100:
        if not number%2 and not number%3:
            sum += number

        number += 1
    print("Sum = {}".format(sum))

# TASK3:
if 0:
    # a3b2v1

    # a3b2v1

    # a3b2v1
    letters = "abv"
    numbers = [3, 2, 1]
    indexes = [0,1,2]

    for c in [0,0,0]:
        for i in indexes:
            print(  "{}{}".format(letters[i], numbers[i]), end=""  )
        print("\n")
    
    for l in letters,letters:
        print(l, i)

# TASK 4:
if 0:
    # ask the user to enter a number, until the number she enters is 5
    # use a do-while simulation    
    while True:
        userNumber = int(input("ENter a number: "))
        print("userNumber == 5: {}".format( userNumber == 5 ))
        if userNumber == 5: break        


#TASK 5:
if 1:
    # user enters a numbers, until 0
    # print the sum of even numbers, entered by the user
    sum = 0
    while True:
        userNumber = int(input("Enter a number: "))
       
        if userNumber == 0:             
            break 
        
        # if userNumber%2: 
        #     continue 
        # sum += userNumber

        if not userNumber%2: 
            sum += userNumber        

    print("Sum is: {}".format(sum))
       
    
            
