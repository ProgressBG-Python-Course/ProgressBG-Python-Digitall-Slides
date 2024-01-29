x = 10  # A global variable

def foo():
    x = 20  # A local variable
    print("Local Scope:", locals())
    print("Global Scope:", globals())

foo()
