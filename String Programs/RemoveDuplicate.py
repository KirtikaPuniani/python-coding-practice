#remove all duplicates from a string

#Using dict.fromkeys
string = 'hello everyone good morning'
result = ''.join(dict.fromkeys(string))    #dict.fromkeys() creates a dictionary with characters of s as keys, automatically removing duplicates.
print(result)
#Efficient because it scans the string once and preserves order.


#Using OrderedDict.fromkeys()
#OrderedDict works similarly to a diction
string = 'hello everyone good morning'
from collections import OrderedDict
result = ''.join(OrderedDict.fromkeys(string))    #OrderedDict.fromkeys() creates an ordered dictionary with characters of s as keys, automatically removing duplicates while preserving order.
print(result)


#using set()
string = 'hello everyone good morning'
output = ''.join(set(string))    #set() creates a set of unique characters, but does not preserve order.
print(output)
#Less efficient because it scans the string and then creates a set, which may not preserve order



#Using a for loop with a set
string = 'hello everyone good morning'
seen = set()    #set to keep track of seen characters
result = ""
for char in string:
    if char not in seen:    #checks if the character has been seen before
        seen.add(char)    #adds the character to the seen set
        result += char    #adds the character to the result string
print(result)



#Using list comprehension with slicing
string = 'hello everyone good morning'
result = ''.join([char for i, char in enumerate(string) if char not in string[:i]])    #enumerate() gives index and character, and slicing checks if the character has appeared before
print(result)