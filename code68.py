# Create class in which one method accept a string and another print it
class print1():
	def __init__(self):
		self.string=""
	def get(self):
		self.string=raw_input("enter string")
	def put(self):
		print("string is ")
		print(self.string)
obj=print1()
obj.get()
obj.put()
	
