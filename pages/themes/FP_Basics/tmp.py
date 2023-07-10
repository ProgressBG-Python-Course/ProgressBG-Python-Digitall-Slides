from functools import reduce
from itertools import product

#TASK: filter only cities which population is greater than 340_000
# cities = [
#       {'name': 'Sofia', 'population': 1_236_000},
#       {'name': 'Plovdiv', 'population': 343_424 },
#       {'name': 'Burgas', 'population': 202_766},
#       {'name': 'Varna', 'population': 335_177},
# ];

# population_iter = map(lambda city: city['population'], cities)

# print(list(population_iter))


# Task: create a list of all user names, which have positive balance, :
# users = [
# 	{'name':'Maria', 'balance': 2000},
# 	{'name':'Petar', 'balance': -189},
# 	{'name':'Ivan', 'balance': 3200},
# 	{'name':'Asen', 'balance': -2890},
# ]

# total_price = reduce( lambda curr_price, product:curr_price+product['price'] ,products, 0)
# print(total_price)

# positive_balance_names = map(lambda user: user['name'] , filter(lambda user: user['balance']>0, users))
# print(list(positive_balance_names))

# numbers = [1,-2, 2, -3, 4]

quotes = [
	'Nothing travels faster than the speed of light, with the possible exception of bad news, which obeys its own special laws',
	'A common mistake that people make when trying to design something completely foolproof is to underestimate the ingenuity of complete fools.'
]

quote = 'A common mistake that people make when trying to design something completely foolproof is to underestimate the ingenuity of complete fools.'

words = map(lambda word: word.upper(),
     	filter(lambda word: word.startswith('t') and len(word)>3,
		reduce(lambda str1, str2: str1+str2, quotes).split()))

for word in words:
	print(word)