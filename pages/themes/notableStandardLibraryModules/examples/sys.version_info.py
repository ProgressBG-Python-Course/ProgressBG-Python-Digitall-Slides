import sys

if sys.version_info[0] == 2:
	print("This program requires Python 3 or above. You are using Python 2.")
elif sys.version_info[0] == 3:
	print("Python 3 is running")