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