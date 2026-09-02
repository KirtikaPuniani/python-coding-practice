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