def user_input(msg):
    try:
        usr_input = input(msg)
        return (usr_input, True)
    except:
        print("User Break - 'CTRL+D' is Disabled!!")
        return ("Not OK", False)


# def user_input(msg):
#     usr_input = input(msg)
#     if len(usr_input)>2:
#         return (usr_input, True)
#     else:
#         print("User Break - 'CTRL+D' is Disabled!!")
#         return ("Not OK" ,False)

while True:
    status = user_input("Enter your message: ")
    # print(x)
    if status[1]:
        quit()
