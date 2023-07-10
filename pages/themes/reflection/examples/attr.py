class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age


maria = Person("Maria Popova", 25)

print(hasattr(maria,"name"))
print(hasattr(maria,"surname"))

print(getattr(maria, "age"))

setattr(maria, "surname", "Popova")
print(getattr(maria, "surname"))
