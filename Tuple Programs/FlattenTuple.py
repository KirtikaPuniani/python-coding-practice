#Flatten tuple of list to tuple
# Given a tuple that contains multiple lists, the task is to flatten it into a single tuple containing all elements from those lists.
# For example:
# Input: ([5, 6], [6, 7, 8, 9], [3])
# Output: (5, 6, 6, 7, 8, 9, 3)



#Using itertools.chain()
#chain.from_iterable() combines multiple inner lists into a single sequence without creating intermediate lists. It is particularly suitable for large datasets, as it lazily iterates over elements, reducing memory consumption
from itertools import chain
tup = ([5, 6], [6, 7, 8, 9], [3])
output = tuple(chain.from_iterable(tup))
print(output)