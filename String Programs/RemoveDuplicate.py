#remove all duplicates from a string

#Using dict.fromkeys
string = 'hello everyone good morning'
result = ' '.join(dict.fromkeys(string))    #dict.fromkeys() creates a dictionary with characters of s as keys, automatically removing duplicates.
print(result)
#Efficient because it scans the string once and preserves order.