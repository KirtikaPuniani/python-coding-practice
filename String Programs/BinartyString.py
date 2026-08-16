#Check if a given string is binary string or not python

#A binary string is a string that contains only the character '0' and '1'. eg: '101010' is binary string while '10201' is not. Task is to check if given string is a binary string or not

#Using all
a = '1010101110001010111000'
if all(x in '01' for x in a):     #all creates a generator that iterates through each char in a. checks if each char belongs to the set {'0', '1'}
    #short circuit evaluation- all stops immediately if a char fails the condition, making it fast for large strings
    print("Yes")
else:
    print("No")
    
    
    
#Using set
a = '1000111001101010101'
if set(a).issubset({'0', '1'}):    #set converts the string into a set of unique chars. issubset checks if all unique chars are either 0 or 1.
    print("Yes")
else:
    print("No")
    
    
    
#Using Regular Expression
import re
s = '10011000022211110000'
if re.fullmatch('[01]+', s):      #[01]+ matches one or more occurences of 0 or 1. fullmatch ensures the entire string matches the pattern. regex is poweful concise but slightly slower than all
    #or set based checks for simple pattern
    print("Yes")
else:
    print("No")
    
    

#Using for loop
s = '101010203000111'
for char in s:
    if char not in '01':
        print("No")
        break
else:
    print("Yes")