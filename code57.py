# to count number of vowels in the string using sets
s= raw_input("Enter the string")
count=0
vowels=set("aeiou")
for letter in s:
	if letter in vowels:
		count= count+1
print("Count of vowels",count)

