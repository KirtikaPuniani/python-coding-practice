#Check if a given string is binary string or not python

#A binary string is a string that contains only the character '0' and '1'. eg: '101010' is binary string while '10201' is not. Task is to check if given string is a binary string or not

#Using all
a = '1010101110001010111000'
if all(x in '01' for x in a):
    print("Yes")
else:
    print("No")