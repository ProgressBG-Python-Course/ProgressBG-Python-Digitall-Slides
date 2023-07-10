"""Even numbers: with and without lambda
"""
# def is_even(x):
#   return True if x!=0 and x%2==0 else False

# even_numbers = list( filter(is_even, range(10)) )


# even_numbers = filter(lambda x: x%2==0 if x!=0 else False, range(10))

# print( list(even_numbers) )


""" filter empty strings """
names = ["Ivan", "", "Alex", "", "Maria", "Angel", ""]
# not_empty_names = filter(lambda s: s, names)
# with list comprehensions
# not_empty_names = [ name for name in names if name]
print( list(not_empty_names) )


# names = ["Ivan", "Alex", "Maria", "Angel", ""]
# filtered_names = filter(lambda s: s and s[0]=="A", names)

# print( list(filtered_names) )







