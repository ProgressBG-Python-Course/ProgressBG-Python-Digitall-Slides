from random import randint
import ptvsd


ptvsd.enable_attach("my_secret", address=('localhost', 3000))

ptvsd.wait_for_attach()

number = randint(1,10)
print(number)
