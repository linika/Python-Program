# to display power of 2 using anonymous function
terms=int(input("HOw many terms"))
result=list(map(lambda x:2**x,range(terms)))
print("the total term is",terms)
for i in range(terms):
	print("2 raised to power",i,"is",result[i])
