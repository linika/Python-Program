# Finding the area of reactangle using classes
class reactangle:
	def __init__(self,breadth,length):
		self.breadth=breadth
		self.length=length
	def area(self):
		return self.breadth*self.length
a=int(input("Enter lenght:"))
b=int(input("Enter bredth:"))
obj=reactangle(a,b)
print("Area of rectangle",obj.area())
