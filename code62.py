# TO read a file and capitalize hte first letter of every word in file
fname=input("Enter the file name")
with open(fname,"r") as :
	for line in f:
		l=line.title()
		print(l)
