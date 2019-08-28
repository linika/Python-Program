# finding the factorial of number

num=int(input("enter the number"))
factorial =1
if num<0:
	print("Sorry, Factorial doesn't exit for this")
elif num==0:
	print("factorail is 1")
else:
	for i in range(1,num+1):
		factorial=factorial*i
	print("the factorial of",num,"is",factorial)	
