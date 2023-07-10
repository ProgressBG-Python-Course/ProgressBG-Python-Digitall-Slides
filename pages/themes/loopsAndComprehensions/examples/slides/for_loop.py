print("{:~^45}".format(" Simple example 1 "))
for s in "ada":
    print(s.capitalize())

print("\n{:~^45}".format(" Simple example 2 "))
for num in [1,2,3,4]:
    print(num)

print("\n{:~^45}".format(" Nested for statements "))
for i in [1,2,3]:
    for j in "abv":
        print(j)
    print("\n") #prints new line 

