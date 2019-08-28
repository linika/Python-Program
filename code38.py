# multiply two matrixes
x=[[12,3,9],[6,8,9],[1,4,6]]
y=[[8,3,9],[6,8,9],[8,4,0]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
	for j in range(len(y[0])):
		for k in range(len(y)):
			result[i][j] += x[i][k]*y[k][j]
for r in result:
	print(r)
