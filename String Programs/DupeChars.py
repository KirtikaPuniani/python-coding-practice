#Find all duplicate chars in a string
#given a string, the task is to find all chars that appear more than once in it.
# For eg: I/P - 'IamKirtikaPuniani'
#         O/P - ['i', 'a', 'n']


#Using collections.Counter
# Counter() function automatically counts how many times each char appears. Then, we can easily extract chars that occur more than once
from collections import Counter
string = 'IamKirtikaPuniani'
d = Counter(string)       #counts each char and stores as {char: count}
result = [i for i, count in d.items() if count > 1]       #d.items() returns key-value pairs of char and frequency. [i for i, count in d.items() if count > 1] filters only duplicate chars
print(result)



#Using loop with dictionary
string = 'IamKirtikaPuniani'
d = {}
result = []
for i in string:
    d[i] = d.get(i, 0) + 1    #d.get(i, 0) returns current count(default is 0) if key doesn't exist
for i, count in d.items():
    if count > 1:
        result.append(i)
print(result)