### Create two list:
fruits = ["apple", "banana", "strawberry"]
numbers = [1,2,3]

### Change list item
fruits[1] = "plum"
print( fruits )
# ['apple', 'plum', 'strawberry']

### Concatenate two lists
print( fruits + numbers )
# ['apple', 'plum', 'strawberry', 1, 2, 3]

### Multiply a list
print( numbers * 3 )

### Delete a list item by index
del fruits[1]
print(fruits)
