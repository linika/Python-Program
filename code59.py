# reading the content of the file
a=str(input("Enter the name of file with .txt extension"))
fil=open(a,r)
line=fil.readline()
while(line!=""):
	print(line)
	line=fil.readline()
fil.close()
