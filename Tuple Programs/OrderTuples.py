#Order tuples by list
# Given a list of tuples, our task is to reorder it according to the sequence defined in another list. This can be useful in data processing, sorting, and mapping tasks


#Using dict + list comprehension
#convert the list of tuples into a dictionary for fast key-value access, then use list comphrehension to reorder tuples based on the given list sequence
tuple = [('apple', 6), ('banana', 8), ('orange', 2), ('strawberry', 4)]
list = ['apple', 'orange', 'banana', 'strawberry']
temp = dict(tuple)         #converts the list of tuples into a dictionary for quick key-value lookup
output = [(key, temp[key]) for key in list]
print(output)