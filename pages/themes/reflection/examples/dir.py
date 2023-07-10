class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

maria = Person("Maria Popova", 25)

print(dir(maria))
print(maria.__dict__)
