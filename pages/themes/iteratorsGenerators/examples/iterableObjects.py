from random import randint

class Employee():
  """docstring for Employee"""
  def __init__(self, name, salary=None):
    self.name = name
    self.salary = salary or randint(100,200)*10

  def __str__(self):
    return "{} - {}".format(self.name, self.salary)

  def present(self):
    print("say hello to {}!".format(self.name))


class Employees():
  """docstring for Employees"""
  def __init__(self):
    self.employees = []
    self.__employees_sorted = []

  def __sort_by_salary(self):
    # print("sorting......................: ", self.employees[0].salary)
    if self.employees:
      # student_list = sorted(student_list, key=lambda student: student.mark)
      self.__employees_sorted = sorted(self.employees, key=lambda o: o.salary, reverse=True)

    return self.__employees_sorted

  def add_new(self, e):
    self.employees.append(e)

  def sorted_by_salary(self):
    return self.__employees_sorted or self.__sort_by_salary()


class NameMaker():
  """docstring for Employee"""

  def __init__(self, limit):
    self.limit = limit
    self.count = 0
    self.vowels = ["а","о","е","и","ю","я"]

  def __gen_random_consonant(self):
    s = chr(randint(1072, 1103))
    while s in self.vowels:
      s = chr(randint(1072, 1103))
    return s

  def __gen_random_vowel(self):
    return self.vowels[randint(0,4)]

  def __gen_random_name(self,i,j):
    ### create random name, between i - j letters long:
    self.name = []
    self.name_length = randint(i,j)

    letter_functions = [self.__gen_random_consonant, self.__gen_random_vowel]

    for i in range(self.name_length):
      # give 50% - 50% chance for a vowel (not quite, but it's ok):
      vowel_chance = randint(0,1)
      self.name.append( letter_functions[vowel_chance]() )

    self.name = "".join(self.name)

    return self.name.capitalize()

  def __iter__(self):
    return self

  def __next__(self):
    name = self.__gen_random_name(3,6)

    if ( self.count < self.limit):
      self.count += 1
      return name
    else:
      raise StopIteration


# make some employees:
employees = Employees()
for name in NameMaker(10):
  employee = Employee(name)
  employees.add_new(employee)


print("employees sorted by salary: ")
for i in employees.sorted_by_salary():
  print(i)







