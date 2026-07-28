#Words Frequency in String Shorthands
#given a string the task is to find how many times each word appears in it.


#Using collections.counter
from collections import Counter
string = 'hello how is everyone this fine morning'
result = Counter(string.split())
print(result)