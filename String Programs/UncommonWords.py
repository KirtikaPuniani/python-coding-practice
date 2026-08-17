#Find uncommon words from two strings
#Extract words that appear in only one of two given strings while ignoring common words.
#eg: s1 = 'Hi I am here' and s2 = 'Hi I am from London'. O/P = []'from', 'London']



#Using collections.Counter
from collections import Counter
s1 = "Hi I am here"
s2 = "Hi I am from London"

count = Counter(s1.split()) + Counter(s2.split())
result = [word for word in count if count[word] == 1]
print(result)



#Using get
s1 = "Hello how are you"
s2 = "Hello what are you doing"
d = {}
for word in (s1 + " " + s2).split():
    d[word] = d.get(word, 0) + 1
result = [word for word in d if d[word] == 1]
print(result)



#Using set
s1 = "Hi I am here"
s2 = "Hi I am from London"
set1 = set(s1.split())
set2 = set(s2.split())
result = list(set1 ^ set2)
print(result)