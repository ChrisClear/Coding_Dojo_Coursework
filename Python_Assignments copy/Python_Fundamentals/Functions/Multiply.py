def multiply(list,multiplier):
	newList = []
	for item in list: 
		item = item * multiplier
		newList.append(item)
	return newList
		
a = [2, 4, 10, 16]
b = multiply(a,5)
print(b);