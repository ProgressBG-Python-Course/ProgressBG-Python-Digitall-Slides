class UserNameError(Exception):
	def __init__(self, value):
	  self.value = value
	def __str__(self):
	  return repr(self.value)

try:
    raise ValueError('Represents a hidden bug, do not catch this')
    raise Exception('This is the exception you expect to handle')
except Exception as error:
    print('Caught this error: ' + repr(error))

