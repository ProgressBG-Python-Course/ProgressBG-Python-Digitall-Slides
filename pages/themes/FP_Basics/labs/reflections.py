class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hi, I'm {}".format(self.name))

class Student(Person):
  def __init__(self,name,subject):
    super().__init__('Person')
    self.subject = subject

  def go_to_school(self):
    pass


pesho  = Student("Pesho", "Math")

print( isinstance(pesho, Person) )












