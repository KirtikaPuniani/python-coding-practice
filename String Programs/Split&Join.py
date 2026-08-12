#Split a string into parts based on a delimeter and then join those parts with a different separator.
#Eg: 'How are you?' split by spaces and joined with hyphens becomes 'How-are-you?'


#Using split and join
string = 'Hello, How are you?'
s = string.split()     #divides the string into a list of words, split by spaces by default
result = '-'.join(s)     #resembles the list into a string with hyphens between the words
print(result)