def numbers_generator(start,end):
  num  = start
  while num<=end:
  	# yield is almost like return, but it freezes the execution
  	yield num
  	num += 1



my_numbers = numbers_generator(1,10)
print(type(my_numbers))

for i in my_numbers:
	print(i)
