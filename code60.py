# copy the content o one file to another file
with open("body.txt") as f:
	with open("out.txt") as f1:
		for line in f:
			f1.write(line)
