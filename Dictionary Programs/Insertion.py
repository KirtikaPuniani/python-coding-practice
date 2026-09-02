#Insertion at the beginning in orderedDict


#Using move_to_end()
from collections import OrderedDict
dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
dict.update({'d': 4})          #adds the new key value pair at the end of the dictionary
dict.move_to_end('d', last=False)          #last = False moves the key to the beginning of the dictionary
print(dict)



#Using Dictioanry unpacking
from collections import OrderedDict
dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
dict = OrderedDict({'d': 4, **dict})         #creates a new dictionary with the new key value pair at the beginning of the dictionary. Converts ot back into an OrderedDict to maintain order explicitly
print(dict)



#Using concatenation of items() 
from collections import OrderedDict
dict = OrderedDict([('a', 1), ('b', 2)])
dict2 = OrderedDict([('c', 3), ('d', 4)])
result = OrderedDict(list(dict2.items()) + list(dict.items()))          #concatenates the items of both dictionaries and creates a new OrderedDict with the new key value pair at the beginning of the dictionary
print(result)



#Using popitem() and update()
from collections import OrderedDict
dict = OrderedDict([('a', 1), ('b', 2)])
x = OrderedDict()

x.update({'c': 3})          #adds the new key value pair to the new dictionary
x.move_to_end('c', last=False)          #moves the new key value pair to the beginning of the new dictionary
while dict:          #iterates through the original dictionary and adds the key value pairs to the new dictionary
    x.update({dict.popitem(last=False)})          #pops the first key value pair from the original dictionary and adds it to the new dictionary
print(x)