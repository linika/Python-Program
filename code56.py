# to remove the key in the dictioanry
d={"a":23,"b":54,"c":89}
print("The Initial dictionary is",d)
key=raw_input("Enter the key to be deleted")
if key in d:
	del d[key]
else:
	print("Key not found")
	exit(0)
print("Updated dictionary",d)

