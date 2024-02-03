def outer():
    x=2

    def inner():
        global x
        x = 3 # we change the global x
        print(f'x = {x} in inner')

    inner()
    print(f'x = {x} in outer')

x = 1
outer()
print(f'x = {x} in global')