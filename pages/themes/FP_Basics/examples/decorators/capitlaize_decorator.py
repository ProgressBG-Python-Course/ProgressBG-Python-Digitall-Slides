def capitalize(func):
  def uppercase():
    result = func()
    return result.upper()
  return uppercase

@capitalize
def greet():
  return "hello"

print(greet())