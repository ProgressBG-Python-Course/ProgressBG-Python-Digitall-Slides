class A():
  # "static" attribute
  count = 0

  def __init__(self, id):
    A.count += 1
  def greed(self):
    print("Hi, I'm ", self.id)


a = A(1)
b = A(99999)
a.count = 666


print( A.count ) #3



