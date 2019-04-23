class MyClass:
	"""A simple example class"""
	i = 12345

        def __init__(self, str):
                self.my_string = str

	def hello(self, name):
                print ("hello" + name)
		return 'hello world'

x = MyClass()

print(x.hello())
