# to remove the punctuation in the string
punc="!()[]{}\/"
my_str="Hello! I am linika."
no_punc=""
for char in my_str:
	if char not in punc:
		no_punc=no_punc+char
print(no_punc) 
