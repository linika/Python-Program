# program to find the number divisible by another number
my_list = [12,35,54,59,694]
result=list(filter(lambda x:(x%13==0),my_list))
print("number divisible by 13 are",result)
