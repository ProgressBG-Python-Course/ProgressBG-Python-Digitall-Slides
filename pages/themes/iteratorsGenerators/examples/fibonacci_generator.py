def fib(count):
    prev = 0
    next = 1
    while count>0:
        value = prev+next
        yield value
        prev, next = next, value
        count-=1


print( list(fib(5)) )