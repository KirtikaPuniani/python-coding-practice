#Count the number of matching characters in a pair of string
#Example: Input: 'hello', 'world'
#Output: 2 (because 'o' and 'l' are common in both strings)



#Using set intersection
s1 = 'hello'
s2 = 'world'
output = len(set(s1.lower()) & set(s2.lower()))     #finds the intersection of both sets and counts the number of common characters
print(output)



#Using list comprehension
s1 = 'apple'
s2 = 'mango'
output = len([char for char in set(s1.lower()) if char in s2.lower()])     #creates a list of common characters and counts them
print(output)



#Using a for loop
s1 = 'kiwi'
s2 = 'grape'

a = s1.lower()
b = s2.lower()
count = 0

for char in set(a):
    if char in b:
        count += 1
print(count)