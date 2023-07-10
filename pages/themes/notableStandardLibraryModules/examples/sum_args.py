import sys

sum = 0

# get only arguments, without the script name
args = sys.argv[1:]

for arg in args:
	sum += int(arg)

print ("The sum of {} is {}".format(args, sum))
