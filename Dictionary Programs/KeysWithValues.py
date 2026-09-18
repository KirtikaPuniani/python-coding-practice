#Keys associated with values in dictionary
#Given a dictionary in Python, our task is to reverse the mapping, i.e., create a new dictionary where each value points to the keys it belongs to. This operation is useful in data organization, analytics, and web applications.
# Input: {'abc': [10, 30], 'bcd': [30, 40, 10]}
# Output: {10: ['abc', 'bcd'], 30: ['abc', 'bcd'], 40: ['bcd']}



#Using defaultdict and loop
from collections import defaultdict
dictionary = {'apple': [1, 2, 3], 'and': [1, 4], 'oranges': [4, 2]}
result = defaultdict(list)        #creates a dictionary where each key automatically starts with an empty list
for key, vals in dictionary.items():
    for v in vals:
        result[v].append(key)        #appends the current key to the list of keys associated with the v
print(dict(result))



#Using dictioanry and loops
dictionary = {'apple': [1, 2, 3], 'and': [1, 4], 'oranges': [4, 2]}
result = {}
for key, vals in dictionary.items():       #iterates over each key–value pair
    for v in vals:
        if v in result:        #checks if the value already exists in the result dictionary
            result[v].append(key)        #adds the current key to the existing list of keys for that value
        else:
            result[v] = [key]
print(result)