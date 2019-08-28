# program to count the number in blank spaces in a text file
fname= input("Enter the file name")
k=0
with open(fname,"r") as f:
	for line in f:
		words =line.split()
		for i in words:
			for letter in i:
				if(letter.isspace):
					k=k+1
print("occurance of blank space")
print(k)
