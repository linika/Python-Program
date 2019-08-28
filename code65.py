# find the area of rectangle using classes

class rectangle():
	def __init__(self,breadth,length):
		self.breadth=breadth
		self.length=length
	def area(self):
		return self.length*self.breadth
a=int(input("Enter the lenght of rectangle"))
b=int(input("Enter the breadth of rectangle"))
obj=rectangle(a,b)
print("Area of rectangle",obj.area())

