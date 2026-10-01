#Sort a List of Tuples by Second Item
# Given a list of tuples, the task is to sort them based on their second element. Each tuple holds ordered data and sorting them by the second item helps organize values in a meaningful order.
# For example:
# Input: [(1, 3), (4, 1), (2, 2)]
# Output: [(4, 1), (2, 2), (1, 3)]

#Using itemgetter
from operator import itemgetter 
a = [(7, 5), (3, 8), (2, 6)]
output = sorted(a, key=itemgetter(1))        #itemgetter(1) retrieves the second item (1) from each tuple. It is more efficient than using a lambda function and sorted() sorts the list based on the second item of each tuple
print(output)



#Using sorted with lambda
a = [(7, 5), (3, 8), (2, 6)]
output = sorted(a, key = lambda x: x[1])
#sorted(a, key=lambda x: x[1]) extract the second element (x[1]) from each tuple for comparison and list is returned in sorted order by the second item of each tuple
print(output)



#Using sort with lambda
a = [(7, 5), (3, 8), (2, 6)]
a.sort(key = lambda x: x[1])        #a.sort(key=lambda x: x[1]) sorts the list a in place based on the second item of each tuple and result is directly stored in the original list a and no new list is created
print(a)


#Using heapq.nsmallest
import heapq
a = [(7, 5), (3, 8), (2, 6)]
output = heapq.nsmallest(len(a), a, key = lambda x: x[1])         #heapq.nsmallest() finds smallest tuples based on the key efficiently. It uses a heap internally, reducing unnecessary comparisons.
print(output)