#Counting frequencies in a list using dictionary


#Using Counter from collections
from collections import Counter
a = ['apple', 'banana', 'kiwi', 'apple', 'grapes', 'banana', 'orange']
frequency = Counter(a)       #counter function creates a dictionary like object where keys are items and values are their counts
print(dict(frequency))       #dict(frequency) converts the Counter object to a standard dictionary



#Using defaultdict
from collections import defaultdict
a = ['apple', 'banana', 'kiwi', 'apple', 'grapes', 'banana', 'orange']
frequency = defaultdict(int)         #defaultdict(int) creates a dictionary where each missing key defaults to 0
for item in a:        #for reach item in a, frequency[item] += 1 increments its count
    frequency[item] += 1
print(dict(frequency))



#Using get method
a = ['apple', 'banana', 'kiwi', 'apple', 'grapes', 'banana', 'orange']
frequency = {}
for item in a:
    frequency[item] = frequency.get(item, 0) + 1        #frequency.get(item, 0) returns the current count of item or 0 if it doesn't exist and adding 1 increments the count
print(frequency)



#Using dictionary
a = ['apple', 'banana', 'kiwi', 'apple', 'grapes', 'banana', 'orange']
frequency = {}
for item in a:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1
print(frequency)