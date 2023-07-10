import traceback

x = 5
y = 3
z = 0

def foo():
	x/y
	x/z


try:
	foo()
except Exception as e:
	print("I'm processing exception: {}".format(e))
	caught = e

print(caught.__traceback__)
traceback.print_tb(caught.__traceback__)


