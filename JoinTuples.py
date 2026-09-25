#Join tuples if similar initial element
#Given a list of tuples, combine (or join) all tuples that share the same first element into a single tuple. The order of remaining elements should be preserved.
#Example:
# Input: [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
# Output: [(5, 6, 7, 8), (6, 10), (7, 13)] 




#Using defaultdict and loop
from collections import defaultdict
tup = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
map = defaultdict(list)
for k, v in tup:
    map[k].append(v)
output = [(k, *v) for k, v in map.items()]
print(output)



#Using itertools.groupby()
from itertools import groupby
tup = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
output = []
for k, g in groupby(tup, key = lambda x: x[0]):
    vals = [v for _, v in g]
    output.append((k, *vals))
print(output)