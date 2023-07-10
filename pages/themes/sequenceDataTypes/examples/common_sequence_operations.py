### Let's have two list:
fruits = ["apple", "banana", "strawberry"]
numbers = [1, 2, 3]

### Concatenation:
concat_list = fruits + numbers
print(concat_list)
# ['apple', 'banana', 'strawberry', 1, 2, 3]

### Repetition
rep_list = numbers * 3
print(rep_list)
# [1, 2, 3, 1, 2, 3, 1, 2, 3]

### Membership Testing (in):
print("banana" in fruits)
# True

print("banana" in numbers)
# False

### Membership Testing (not in):
print("banana" not in fruits)
# False

print("banana" not in numbers)
# True

r = range(0,10)
print(3 in r)


### Indexing
str = "abcde"
print(str[-1])
# e

### Slicing
print("Slicing")
str = "abcdef"
print(str[0:2])
# ab

print(str[])

print(str[0:-1])
# abcde

print(str[0:-1:2])
# ace

print(str[-1:-4:-1])
# fed

print(str[-1::-1])
# fedcba

print(str[::])



print(str)


