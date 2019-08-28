# add two matrix
x=[[12,7,6],[3,5,8],[9,8,3]]
y=[[9,5,8],[6,3,2],[6,9,8]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
	for j in range(len(x[0])):
		result[i][j]=x[i][j]+y[i][j]
for r in result:
	print(r)

