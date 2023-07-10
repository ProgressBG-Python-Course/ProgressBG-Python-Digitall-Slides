"""map numbers in a list to a list of squared numbers"""
# numbers = [1,2,3,4,5]

# sqr_numbers = map(lambda x:x**2, numbers)

# print( list(sqr_numbers) )

""" generate all uppercase cyrillic letters by their UTF codes """
# letters = map(chr, range(1040, 1072))
# print( list(letters) )


""" map each small letter 'a' in a string to upper-case letter 'A' """
# phrase = "alabala"
# new_phrase  = map(lambda s: s.capitalize() if s=="a" else s , phrase)

# print(list(new_phrase))

""" sum elements of two lists """

# def add(a,b):
#   print("a = ", a)
#   print("b = ", b)

#   return a+b

l1 = [1,2,3]
l2 = [1,2,3]

l_sum = map(lambda *t: a+b, l1, l2)
print( list(l_sum) )
