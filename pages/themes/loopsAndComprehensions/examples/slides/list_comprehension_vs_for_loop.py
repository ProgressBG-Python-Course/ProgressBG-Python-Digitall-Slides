import time

def evens_with_for(l):
	evens = []
	for el in l:
		if(el%2==0):
			evens.append(el)

	return evens

def evens_with_comprehensions(l):
	return [el for el in l if el%2==0]


r = range(10_000_000)

start = time.time()
evens_with_for(r)
print('evens_with_for took: ', time.time() - start)

start = time.time()
evens_with_comprehensions(r)
print('evens_with_comprehensions took: ', time.time() - start)

# evens_with_comprehensions(r)