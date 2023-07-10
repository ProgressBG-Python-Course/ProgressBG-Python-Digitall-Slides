### Create list of fruits:
fruits = ["apple", "banana", "strawberry"]

### Appends item the end of the list:
fruits.append("plum")
print(fruits)
# ['apple', 'banana', 'strawberry', 'plum']

### Insert item in specified position (by the index given as first parameter) 
fruits.insert(2, "NEW")
print(fruits)
# ['apple', 'banana', 'NEW', 'strawberry', 'plum']

### Retrieve the item at the end and remove it from the list:
item = fruits.pop() 
print(item, fruits)
# plum ['apple', 'banana', 'NEW', 'strawberry']

### Retrieve the item at the index given and remove it from the list:
item = fruits.pop(2)
print(item, fruits)
# NEW ['apple', 'banana', 'strawberry']

### Remove the first item from a list by the given value:
fruits.remove("banana")
print(fruits)
# ['apple', 'strawberry']

### Reverse the items of a list in place:
fruits.reverse()
print(fruits)
# ['strawberry', 'banana', 'apple']
