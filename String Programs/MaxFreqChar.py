#Find the character in a string that appears the most number of times


#Using collections.Counter
from collections import Counter
string = 'hello everyone good morning'
frequency = Counter(string)
most_freq_count = max(frequency, key = frequency.get)     #finds the maximum frequency count
print(most_freq_count)



#Using set and counter
from collections import Counter
string = 'I am so pissed off with this assignment'
string = string.replace(" ", "")        #strip spaces from the string which will not be possible if we use set() as it will consider space as a character and will give wrong output. Without 
# this line, the output will be space as it is the most frequent character in the string.
max_char = max(set(string), key = Counter(string).get)     #finds the maximum frequency count
print(max_char)



#Using dict.get() with max()
string = 'It is a beautiful day to save lives'
string = string.replace(" ", "")        #strip spaces from the string which will not be possible if we use set() as it will consider space as a character and will give wrong output. Without 
# this line, the output will be space as it is the most frequent character in the string
freq = {}
for char in string:
    freq[char] =freq.get(char, 0) + 1
max_char = max(freq, key = freq.get)     #finds the maximum frequency count
print(max_char)



#Using str.count()
string = '''It's a pleasure to meet you. I am a software engineer and I love coding.'''
max_char = ''
max_count = 0
for char in set(string):
    string = string.replace(" ", "") 
    count = string.count(char)
    if count > max_count:
        max_count = count
        max_char = char
print(max_char)


