#Count the number of matching characters in a pair of string
#Example: Input: 'hello', 'world'
#Output: 2 (because 'o' and 'l' are common in both strings)



#Using set intersection
s1 = 'hello'
s2 = 'world'
output = len(set(s1.lower()) & set(s2.lower()))     #finds the intersection of both sets and counts the number of common characters
print(output)