#Words Frequency in String Shorthands
#given a string the task is to find how many times each word appears in it.


#Using collections.counter
from collections import Counter
string = 'hello how is everyone this fine morning'
result = Counter(string.split())    #counter automatically counts how many rimes each word appears in a listwhen we split the string into words.
print(result)