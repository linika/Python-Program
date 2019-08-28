# program to sort the list o tuples in increasing order by last elemnet in each tuple

def last(n):
	return n[-1]
def sort(tuples):
	return sorted (tuples,key=last)
a=input("enter the list of tuples")
print("sorted")
print(sort(a))
