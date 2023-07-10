class Base:
	def __init__(self):
		print('Base instance created!')

	def foo(self):
		print(f'foo() in Base is called! Working on {self.name}')

class Child1(Base):
	def __init__(self, name):
		self.name = name

		# call Base foo() method. Reference to self is passed implicitly
		super().foo()


ch1 = Child1('ch1')