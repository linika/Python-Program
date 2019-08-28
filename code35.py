#convert decimal to binary using recursion
def convertToBinary(n)		:
	if n>1:
		convertToBinary(n//2)
	print(n%2,end="")# this will help to come in horizontal line
dec=34
convertToBinary(dec)

