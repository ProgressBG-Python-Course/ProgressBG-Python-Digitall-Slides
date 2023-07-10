def stars_decorator(f,x):
	def wrapper(user):
		print("*" * 50)
		f(user)
		print("*" * 50)

	return wrapper

# let's decorate greet:
@stars_decorator
def greet(user):
	print(f"Howdy {user}!")

# greet = stars_decorator(greet,1)

# and use it:
greet('Ada')