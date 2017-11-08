#new list
x = [19,2,54,-2,7,12,98,32,10,-3,6]
print x
x.sort()
print x
midpoint = len(x)/2


list1 = x[:midpoint]
list2 = x[midpoint:]

list2.insert(0,list1)
print list2
