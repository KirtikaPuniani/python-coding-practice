#Words Frequency in String Shorthands
#given a string the task is to find how many times each word appears in it.


#Using collections.counter
from collections import Counter
string = 'hello how is everyone this fine morning'
result = Counter(string.split())    #counter automatically counts how many rimes each word appears in a listwhen we split the string into words.
print(result)


#using dict.get() with a fpr loop
string = 'hello hello everyone'
result = {}
for word in string.split():     #iterates through each word
    result[word] = result.get(word, 0) + 1    #freq.get() fetches the word's count. the count is incremented by 1 for every occurence
print(result)



#Using defaultdict(int) from collections
from collections import defaultdict
string = 'hello hello everyone'
result = defaultdict(int)         #automatically starts each new key with 0
for word in string.split():
    result[word] += 1            #for each word, increments the count
print(dict(result))





#Using list comprehension with collections.Counter
#Counter allows you to efficiently count the frequecy of the elements by transforming the data and applying counter to generate frequency counts.
from collections import Counter
string = 'hello hello everyone'
result = Counter([word for word in string.split()])     #creates a list of all words and copunter() then counts each word's occurence
print(result)