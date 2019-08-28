# to form new string made up of first 2 and last 2 character from given string
string=raw_input("Enter the string")
count=0
for i in string:
	count=count+1
new=string[0:2]+string[count-2:count]
print("Newly form string is")
print(new)
