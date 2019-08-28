# to check substring is present in given string(this is running online)
strg=input("enter the string")
sub_str=input("enter the sub string")
if (strg.find(sub_str)==-1):
	print("substring not found in the string")
else:
	print("substring found in the string")
