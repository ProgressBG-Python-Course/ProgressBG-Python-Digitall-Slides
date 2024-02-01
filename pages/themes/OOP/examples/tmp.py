class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old. ")

class Employee(Person):
    def greet(self):
        print(f"Hi, I'm the employee {self.name},  {self.age} years old. ")

maria = Person("Maria", 20)
petar = Employee('Petar', 34)

maria.greet()
petar.greet()

# Hi, I'm Maria and I'm 20 years old.
# Hi, I'm the employee Petar,  34 years old.