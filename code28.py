# find the factors of number
def factorr(x):
	print("the factors of number are:")
	for i in range(1,x+1):
		if x%i==0:
			print(i)
num=int(input("enter the number :"))
print(factorr(num))	
