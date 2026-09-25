#Join tuples if similar initial element
#Given a list of tuples, combine (or join) all tuples that share the same first element into a single tuple. The order of remaining elements should be preserved.
#Example:
# Input: [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
# Output: [(5, 6, 7, 8), (6, 10), (7, 13)] 




#Using defaultdict and loop
from collections import defaultdict
tup = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
map = defaultdict(list)            #defaultdict(list) - creates empty lists automatically
for k, v in tup:
    map[k].append(v)               #mapp[k].append(v) - groups values by their first elemen
output = [(k, *v) for k, v in map.items()]          #[(k, *v) ...]: converts grouped data back to tuples.Using dictionary + list comprehension
print(output)



#Using itertools.groupby()
from itertools import groupby
tup = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
output = []
for k, g in groupby(tup, key = lambda x: x[0]):          #groupby(t, key=lambda x: x[0]): groups by first element
    vals = [v for _, v in g]            #vals = [v for _, v in g]: collects second elements
    output.append((k, *vals))         #res.append((k, *vals)): forms combined tuples
print(output)