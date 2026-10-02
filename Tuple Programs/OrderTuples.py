#Order tuples by list
# Given a list of tuples, our task is to reorder it according to the sequence defined in another list. This can be useful in data processing, sorting, and mapping tasks


#Using dict + list comprehension
#convert the list of tuples into a dictionary for fast key-value access, then use list comphrehension to reorder tuples based on the given list sequence
tuple = [('apple', 6), ('banana', 8), ('orange', 2), ('strawberry', 4)]
list = ['apple', 'orange', 'banana', 'strawberry']
temp = dict(tuple)         #converts the list of tuples into a dictionary for quick key-value lookup
output = [(key, temp[key]) for key in list]          #creates a new list of tuples arranged according to the order in o1
print(output)




#Using setdefault + sorted + lambda
tuple = [('apple', 6), ('banana', 8), ('orange', 2), ('strawberry', 4), ('kiwi', 10)]
list = ['apple', 'kiwi', 'orange', 'banana', 'strawberry']
temp = {}
for key, element in enumerate(list):
    temp.setdefault(element, []).append(key)
output = sorted(tuple, key = lambda element: temp[element[0]].pop())
print(output)