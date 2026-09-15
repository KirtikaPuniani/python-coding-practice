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