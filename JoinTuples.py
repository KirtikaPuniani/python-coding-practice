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



#Using dictionary and list comprehension
tup = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
temp = {}
for x in tup:
    temp[x[0]] = temp.get(x[0], []) + list(x[1:])         #temp.get() function Returns current values or initializes an empty list. ## + list(x[1:]): Adds tuple elements to the existing list ### (k,) + tuple(v): Combines key and grouped values.
output = [(k,) + tuple(v) for k, v in temp.items()]
print(output)



#Using recursion
def join_tup(tup, i):
    if i == len(tup) - 1:
        return tup
    elif tup[i][0] == tup[i+1][0]:           
        tup[i] += tup[i+1][1:]
        tup.pop(i+1)
        return join_tup(tup, i)
    else:
        return join_tup(tup, i+1)
tup = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
output = join_tup(tup, 0)
print(output)



def join_tup(tup, i):
    if i == len(tup) - 1:
        return tup
    elif tup[i][0] == tup[i+1][0]:           #Checks if consecutive tuples share the same key
        tup[i] += tup[i+1][1:]           #Merges next tuple’s values
        tup.pop(i+1)        #removes the merged tuple
        return join_tup(tup, i)
    else:
        return join_tup(tup, i+1)
tup = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
output = join_tup(tup, 0)
print(output)