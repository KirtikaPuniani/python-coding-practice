#Extract unique values dictionary values


#Using set and sum
d = {'gfg' : [5,6,7,8],
     'is' : [10,11,7,5], 
     'best' : [6,12,10,8], 
     'for' : [1,2,5]}
res = list(set(sum(d.values(), [])))      #data.values(): fetches all value lists.
#sum(..., []): flattens nested lists by concatenation.
#set(): removes duplicate elements.
#list(): converts the set into a list.
print(res)




#Using set comprehension + values + sorted
d = {'gfg' : [5,6,7,8],
     'is' : [10,11,7,5], 
     'best' : [6,12,10,8], 
     'for' : [1,2,5]}
result = list(sorted({ele for val in d.values() for ele in val}))       #nested set comprehension flattens and removes duplicates. sorted returns a sorted list of unique values
print(result)



#Using chain + set + sorted
from itertools import chain
d = {'gfg' : [5,6,7,8],
     'is' : [10,11,7,5], 
     'best' : [6,12,10,8], 
     'for' : [1,2,5]}
result = list(sorted(set(chain(*d.values()))))        #chin(*data.values()) flattens all value lists without creating intermediate lists
print(result)



#Using counter + append + sort
from collections import Counter
d = {'gfg' : [5,6,7,8],
     'is' : [10,11,7,5], 
     'best' : [6,12,10,8], 
     'for' : [1,2,5]}
vals = [x for v in d.values() for x in v]         #flattens all values
frequency = Counter(vals)        #counts frequency if each element
result = sorted(list(frequency.keys()))       #frequency.keys() retreives unique elements
print(result)




#Using extend + if not in + sort
d = {'gfg' : [5,6,7,8],
     'is' : [10,11,7,5], 
     'best' : [6,12,10,8], 
     'for' : [1,2,5]}
x, result = [], []
for value in d.values():
    x.extend(value)
for y in x:
    if y not in result:
        result.append(y)
result.sort()
print(result)