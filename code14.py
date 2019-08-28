# find the largest among three
num1=float(input("enter the first number"))
num2=float(input("enter the second number"))
num3=float(input("enter the third number"))
if (num1>=num2):
	num=num1
else:
	num=num2
if (num3>=num):
	num=num3
	print("the Largest number is ",num)
else:
	print("the Largest number is ",num)
