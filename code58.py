# program to check common letter in two input string
s1=raw_input("Enter the first string")
s2=raw_input("Enter the second string")
a=list(set(s1)&set(s2))
print("the common letter in both are:")
for i in a:
	print(i)
