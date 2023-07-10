class EvensRange:
  def __init__(self,min,max):
    self.num = 2

  def __next__(self):
    self.num += 2
    return self.num

  def __iter__(self):
    return self


evens = EvensRange(1, 9)

for i in evens:
  print(i)

# 2, 4, 6, 8