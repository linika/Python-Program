#To find the prime number for the range

lower=int(input("Enter the lower range"))
upper=int(input("Enter the higher range"))
print("prime number between ",lower," and",upper,"are")
for num in range(lower,upper+1):
	if num>1:
		for i in range(2,num):
			if(num%i)==0:
				break
			else:
				print(num)
				break
