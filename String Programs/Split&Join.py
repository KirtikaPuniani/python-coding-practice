#Split a string into parts based on a delimeter and then join those parts with a different separator.
#Eg: 'How are you?' split by spaces and joined with hyphens becomes 'How-are-you?'


#Using split and join
string = 'Hello, How are you?'
s = string.split()
result = '-'.join(s)
print(result)