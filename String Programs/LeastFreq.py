#Identify the character that appears least number of times


#Using collections.Counter
from collections import Counter
string = 'hello everyone good morning'
counter = Counter(string)
least_frequent_char = min(counter, key = counter.get)     #finds the character with the minimum count
print(least_frequent_char)



#Using a dictionary to count occurrences
string = 'hello everyone good morning'
char_count = {}
for char in string:
    char_count[char] = char_count.get(char, 0) + 1     #counts occurrences of each character
least_frequent_char = min(char_count, key = char_count.get)     #finds the character with the minimum count
print(least_frequent_char)



#Using sorting
string = 'hello everyone good morning'
char_count = {}
for char in string:
    char_count[char] = char_count.get(char, 0) + 1     #counts occurrences of each character
sorted_freq = sorted(char_count.items(), key=lambda x: x[1])     #sorts the characters by their frequency
least_frequent_char = sorted_freq[0][0]     #gets the character with the least frequency
print(least_frequent_char)