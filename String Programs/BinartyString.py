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
if set(a).issubset({'0', '1'}):
    print("Yes")
else:
    print("No")