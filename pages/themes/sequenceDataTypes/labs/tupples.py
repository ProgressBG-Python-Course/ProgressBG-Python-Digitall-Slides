string = "abcde"

# TASK: 
letter = "c"

# if letter in string:
#     #  (True, 2) 
# else: 
#     # (False)


t = (False,)

# for i in range(len(string)):
#     if letter == string[i]:
#         t = (True, i) 
#         break


# for t in enumerate(string):
#     print(t)
#     if letter == t[1]:
#         t = (True, t[0]) 
#         break

for i,l in enumerate(string):    
    if letter == l:
        t = (True, i) 
        break

print(t)
    
