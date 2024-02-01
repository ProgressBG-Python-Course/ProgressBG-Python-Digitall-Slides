def outer():
    x=2

    def inner():
        nonlocal x
        x = 3 # we change the x in outer
        print(f'x = {x} in inner')

    inner()
    print(f'x = {x} in outer')

x = 1
outer()
print(f'x = {x} in global')

#x = 3 in inner
#x = 2 in outer
#x = 1 in global