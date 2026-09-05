#Sort Python Dictionary by key or value


#Sorting by value
dict = {'watermelon': 10, 'apple': 5, 'banana': 7, 'grapes': 3}
asc = {k: v for k, v in sorted(dict.items(), key = lambda item: item[1])}
print(asc)          #Sorts the dictionary by its values in ascending order using sorted() with a lambda function as the key, and constructs a new dictionary with the sorted items.


#Using OrderedDict
from collections import OrderedDict
dict = {'watermelon': 10, 'apple': 5, 'banana': 7, 'grapes': 3}
asc = OrderedDict(sorted(dict.items(), key = lambda item: item[1]))          #Sorts the dictionary by its values in ascending order using
#sorted() with a lambda function as the key, and constructs an OrderedDict to maintain the sorted order.
print(asc)