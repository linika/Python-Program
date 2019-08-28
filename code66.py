# cerate the class and compute the area and perimeter of rectangle
import math
class circle():
	def __init__ (self,radius):
		self.radius=radius
	def area(self):
		return math.pi*(self.radius**2)
	def perimeter(self):
		return 2*math.pi*self.radius
r=int(input("Enter radius"))
obj=circle(r)
print("Area of circle",round(obj.area(),2))# here we use the round function to round the figure
print("perimeter of cicle",round(obj.perimeter(),2))
