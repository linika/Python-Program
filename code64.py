# progrm to append delete and display elements of list using classes
class check():
	def __init__(self):
		self.n=[]
	def add(self,a):
		return self.n.append(a)
	def remove(self,b):
		self.n.remove(b)
	def dis(self):
		return (self.n)
obj=check()
choice=1
while choice!=0:
	print("o.exit")
	print("1.add")
	print("2.delete")
	print("3.display")
	choice=int(input("enter choice"))
	if choice==1:
		n=int(input("Enter the number to append"))
		obj.add(n)
		print("List",obj.dis())
	elif choice==2:
		n=int(input("Enter the number to remove"))
		obj.remove(n)
		print("List",obj.dis())
	elif choice==3:
		print("List",obj.dis())
	elif choice==0:
		print("Exiting")
	else:
		print("Invalid Choices")
print()

