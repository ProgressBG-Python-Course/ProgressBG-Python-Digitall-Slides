class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

maria = Person("Maria Popova", 25)

print(type(maria))


Employee = type('Employee', (Person,), dict())
pesho = Employee("Pesho", 30)
print(type(pesho))

# pesho.name = "Pesho"
print(dir(pesho))
