#Sort the values of first list using second list in Python

list1 = ['a', 'c', 'b', 'd', 'e']
list2 = [10, 40, 20, 30, 50]

#Using zip() and sorted()
result = [x for _, x in sorted(zip(list2, list1))]
print(result)