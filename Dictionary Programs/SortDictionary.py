#Sort Python Dictionary by key or value


#Sorting by value

#Using sorted()
dict = {'watermelon': 10, 'apple': 5, 'banana': 7, 'grapes': 3}
asc = {k: v for k, v in sorted(dict.items(), key = lambda item: item[1])}
print(asc)          #Sorts the dictionary by its values in ascending order using sorted() with a lambda function as the key, and constructs a new dictionary with the sorted items.


#Using OrderedDict
from collections import OrderedDict
dict = {'watermelon': 10, 'apple': 5, 'banana': 7, 'grapes': 3}
asc = OrderedDict(sorted(dict.items(), key = lambda item: item[1]))          #Sorts the dictionary by its values in ascending order using
#sorted() with a lambda function as the key, and constructs an OrderedDict to maintain the sorted order.
print(asc)


#Using for loop wwith sorted()
dict = {'watermelon': 10, 'apple': 5, 'banana': 7, 'grapes': 3}
for k, v in sorted(dict.items(), key = lambda item: item[1]):          #Iterates through the sorted items of the dictionary by value using sorted() with a lambda function as the key.
    print((k, v), end = ' ')          #Prints each key-value pair in ascending order of values.
    

#Using Numpy
import numpy as np
dict = {'watermelon': 10, 'apple': 5, 'banana': 7, 'grapes': 3}
k = list(dict.keys())          #Extracts the keys of the dictionary into a list.
v = list(dict.values())          #Extracts the values of the dictionary into a list.
index = np.argsort(v)          #Uses numpy's argsort() to get the indices that would sort the values list in ascending order.
sorted_dict = {k[i]: v[i] for i in index}          #Constructs a new dictionary by iterating through the sorted indices and mapping the corresponding keys and values.
print(sorted_dict)          #Prints the new dictionary sorted by values in ascending order.