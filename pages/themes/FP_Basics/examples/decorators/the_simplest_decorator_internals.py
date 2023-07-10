def stars_decorator(f):
	def wrapper():
		print("*" * 50)
		f()
		print("*" * 50)

	return wrapper

def greet():
	print("Howdy World!")

# let's decorate greet:
greet = stars_decorator(greet)

# and use it:
greet()