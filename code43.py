# count the vowel in each number
vowel="aeiou"
ip_str=input("Enter the string")
ip_str=ip_str.casefold()
count={}.fromkeys(vowel,0)
# here in fromkeys we are constructing new dictinary where all the vowels are keys and intialize value as 0
for char in ip_str:
	if char in count:
		count[char]+=1
print(count)
