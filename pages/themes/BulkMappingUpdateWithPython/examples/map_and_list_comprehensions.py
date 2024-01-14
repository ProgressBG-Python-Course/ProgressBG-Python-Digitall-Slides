numbers = [1, 2, 3, 4, 5]

squared = [x**2 for x in numbers]
squared_by_map = map(lambda x: x**2, numbers)

print(squared)
print(list(squared_by_map))

