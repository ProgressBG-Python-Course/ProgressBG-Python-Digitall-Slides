# # strings are iterable in Python:
# s = "abc"

# # iterate over the string iterable with for loop
# for i in s:
#     print(i)

# strings are iterable in Python:
s = "abc"

# lets get an iterator from the string iterable:
s_iterator = iter(s)

#ask the string iterator for values
print( next(s_iterator) )
print( next(s_iterator) )
print( next(s_iterator) )