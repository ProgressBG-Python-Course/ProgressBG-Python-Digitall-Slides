#define the generator function:
def numbers_generator(start,end):
    """Generates numbers from start (inclusive) to end (inclusive)."""
    num  = start
    while num<=end:
        yield num
        num += 1

my_numbers = numbers_generator(1,10)
# iterate over our generator:
for x in my_numbers:
    print(x, end=",")