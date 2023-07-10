data = [
    ["a", "b", "c"],
    [1,2,3]
]
# print("{}{}".format(data[0][2],data[1][2]))
# Task5: print:
# a3
# b2
# c1

# range(3) == [0,1,2]

# for i in range(3):
#     for l in data:
#         print(l[i],end="-") 
#     print("\n")


for i in [0,1,2]:
    print(data[0][i],data[1][i])

