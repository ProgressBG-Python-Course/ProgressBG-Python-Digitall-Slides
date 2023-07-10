### create tuple of 3 elements:
point3d = (4, 0, 3)

print(point3d[0], point3d[1], point3d[2])
# 4 0 3

print(point3d[-1], point3d[-2], point3d[-3])
# 3 0 4

### retrieve tuple items
address = ('Bulgaria', 'Sofia', 'Nezabravka str', 14)

country = address[0]
town = address[1]
street = address[2]
street_num = address[3]
print(country, town, street, street_num)
# Bulgaria Sofia Nezabravka str 14


### change a tuple item:
# address[0] = "France"
# TypeError: 'tuple' object does not support item assignment

### create tuple with 3 elements:
ada_birth_date = (10, "December", 1815)

# retrieve tuple elements:
ada_birth_day = ada_birth_date[0]
ada_birth_month = ada_birth_date[1]
ada_birth_year = ada_birth_date[2]

print("Ada is born on {} {} in {}".format(ada_birth_month, ada_birth_day, ada_birth_year))
# Ada is born on December 10 in 181
