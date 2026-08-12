#Split a string into parts based on a delimeter and then join those parts with a different separator.
#Eg: 'How are you?' split by spaces and joined with hyphens becomes 'How-are-you?'


#Using split and join
string = 'Hello, How are you?'
s = string.split()     #divides the string into a list of words, split by spaces by default
result = '-'.join(s)     #resembles the list into a string with hyphens between the words
print(result)




#Using re.split and '-'.join
#in cases needing advanced splitting, eg, handling multiple spaces or different delimeters re.split from the re module offers more flexibility. However its less efficient than split for 
#simple cases due to the overhead of regyular expression processing.

import re
string = 'Hello, How are you?'
s = re.split(r'\s+', string)     #split by spaces
a = '-'.join(s)    #join with a hyphen
# print(s)
print(a)