# To count number of lowercase character in a string
count=0
str=raw_input("enter the string")
for i in str:
	if(i.islower()):
		count=count+1
print("the number of lowercase character are")
print(count)
