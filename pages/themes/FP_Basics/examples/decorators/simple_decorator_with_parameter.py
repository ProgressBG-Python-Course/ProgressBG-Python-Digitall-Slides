def stars_decorator(f):
	def wrapper(n):
		print("*" * 50)
		f(n)
		print("*" * 50)

	return wrapper

# let's decorate greet:
@stars_decorator
def greet(name):
	print("Howdy {}!".format(name))


# and use it:
greet("Pesho")