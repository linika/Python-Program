# to find the fibonacci sequence 
#not working in this but online it will work

nterms=int(input("enter the terms"))
n1=0
n2=1
count=0
if nterms<=0:
	print("enter the positive number")
elif nterms==1:
	print("fabonacci sequence upto",nterms,":")
	print(n1)
else:
	print("fabonacci sequence upto",nterms,":")
	while count<nterms:
		print(n1,end=",")
		nth=n1+n2
		n1=n2
		n2=nth
		count+=1
