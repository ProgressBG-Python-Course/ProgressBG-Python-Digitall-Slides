from datetime import datetime

def timestamp(f):
	def wrapper():
		# do something before function call
		dtstr = str(datetime.now())
		print( dtstr.center(50, "~") )
		f()
		print(" f() was called".center(50, "~"))
	return wrapper


def greet():
	print("Hello ")

# decorate greet
greet = timestamp(greet)

# use decorated greet
greet()
