# TO remove the character of odd index
def modify(string):
	final=""
	for i in range(len(string)):
		if i%2==0:
			final=final+string[i]
	return final
string=raw_input("Enter the string")
print(modify(string))
