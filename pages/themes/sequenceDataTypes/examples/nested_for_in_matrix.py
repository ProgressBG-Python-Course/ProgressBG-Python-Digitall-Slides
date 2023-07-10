print("\n{:~^45}".format(" Nested for statements "))
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for el in row:
        print(el)
