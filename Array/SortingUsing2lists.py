#Sort the values of first list using second list in Python

#Given two lists of equal length, where the second list defines the order, the task is to reorder the first list according to the sorted order 
#of the second list.

list1 = ['a', 'c', 'b', 'd', 'e']
list2 = [10, 40, 20, 30, 50]

#Using zip() and sorted()
result = [x for _, x in sorted(zip(list2, list1))]
print(result)



#Using numpy.argsort()

import numpy as np
list1 = ['a', 'c', 'b', 'd', 'e']
list2 = [10, 40, 20, 30, 50]

result = [list1[i] for i in np.argsort(list2)]
print(result)