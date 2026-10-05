#Flatten tuple of list to tuple
# Given a tuple that contains multiple lists, the task is to flatten it into a single tuple containing all elements from those lists.
# For example:
# Input: ([5, 6], [6, 7, 8, 9], [3])
# Output: (5, 6, 6, 7, 8, 9, 3)



#Using itertools.chain()
#chain.from_iterable() combines multiple inner lists into a single sequence without creating intermediate lists. It is particularly suitable for large datasets, as it lazily iterates over elements, reducing memory consumption
from itertools import chain
tup = ([5, 6], [6, 7, 8, 9], [3])
output = tuple(chain.from_iterable(tup))           #chain.from_iterable(tup) - iterates through each sublist inside tup and extracts their elements in sequence AND tuple() converts the flattened sequence into a tuple
print(output)



#Using list comprehension
tup = ([5, 6], [6, 7, 8, 9], [3])
output = tuple(x for sublist in tup for x in sublist)
# for sublist in tup loops through each inner list.
# for x in sublist accesses each element inside the sublist.
# x extracts individual elements.
# tuple() converts the flat sequence into a tuple.
print(output)




#Using functools.reduce()
from functools import reduce
tup = ([5, 6], [6, 7, 8, 9], [3])
output = tuple(reduce(lambda x, y: x + y, tup))       
#reduce(lambda x, y: x + y, tup) combines all sublists in tup by repeatedly concatenating pairs of sublists into a single list and tuple() converts the result into a flattened tuple of elements
print(output)




#Using sum()
tup = ([5, 6], [6, 7, 8, 9], [3])
output = tuple(sum(tup, []))   #sum(tup, []) concatenates all sublists in tup into a single list, starting with an empty list [], and tuple() converts the result into a flattened tuple of elements
print(output)
