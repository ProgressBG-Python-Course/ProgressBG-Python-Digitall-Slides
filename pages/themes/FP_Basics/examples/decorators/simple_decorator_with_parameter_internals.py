def stars_decorator(f):
	def wrapper(n):
		print("*" * 50)
		f(n)
		print("*" * 50)

	return wrapper

def greet(name):
	print("Howdy {}!".format(name))

# let's decorate greet:
greet = stars_decorator(greet)

# and use it:
greet("Pesho")