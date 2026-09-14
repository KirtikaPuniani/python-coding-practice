#Counting frequencies in a list using dictionary


#Using Counter from collections
from collections import Counter
a = ['apple', 'banana', 'kiwi', 'apple', 'grapes', 'banana', 'orange']
frequency = Counter(a)
print(dict(frequency))