#Find the character in a string that appears the most number of times


#Using collections.Counter
from collections import Counter
string = 'hello everyone good morning'
frequency = Counter(string)
most_freq_count = max(frequency, key = frequency.get)     #finds the maximum frequency count
print(most_freq_count)
