#Extract digits from tuple list
#Given a list of tuples containing numbers of varying lengths, the task is to extract all unique digits present in those tuples
#Example:
# Input: list = [(15, 3), (3, 9)] 
# Output: [9, 5, 3, 1]

# Input: list = [(15, 3)] 
# Output: [5, 3, 1] 



#Using list comprehension and set
tup = [(15, 3), (3, 9), (1, 10), (99, 2)] #[(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
temp = ''.join([str(i) for x in tup for i in x])             #Converts each number in all tuples to a string and join function joins all string numbers into one continuous string
output = [int(i) for i in set(temp)]         #set(temp) removes duplicate digits.   ##[int(i) for i in set(temp)] - converts unique string digits back to integers
print(output)



#Using map + chain.from_iterable + set
from itertools import chain
tup = [(15, 3), (3, 9), (1, 10), (99, 2)]
x = map(str, chain.from_iterable(tup))         #chain.from_iterable(tup)flattens all tuples into a single sequence.    ##map() function converts each number to a string
output = {d for n in x for d in n}       #Extracts individual digits and keeps only unique ones
print(output)



#Using regex
import re
tup = [(15, 3), (3, 9), (1, 10), (99, 2)]
reg = re.sub(r'[\[\]\(\), ]', '', str(tup))      #str() function converts tuple to string.    ##re.sub() removes brackets, commas and scpaces/
output = [int(i) for i in set(reg)]          #set(reg) collects unique digit characters.   ##int(i) for i in converts them back to integers
print(output)



#Using nested loops + set
tup = [(15, 3), (3, 9), (1, 10), (99, 2)]
a = ''
for x in tup:
    for y in x:
        a += str(y)
output = list(map(int, set(a)))
print(output)