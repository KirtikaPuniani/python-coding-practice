#Counting frequencies in a list using dictionary


#Using Counter from collections
from collections import Counter
a = ['apple', 'banana', 'kiwi', 'apple', 'grapes', 'banana', 'orange']
frequency = Counter(a)       #counter function creates a dictionary like object where keys are items and values are their counts
print(dict(frequency))       #dict(frequency) converts the Counter object to a standard dictioanry