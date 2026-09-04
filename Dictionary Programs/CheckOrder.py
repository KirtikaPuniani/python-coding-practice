#Check order of character in string using OrderedDict()


#Using orderedDict() with index mapping
from collections import OrderedDict
string = 'Engineers Rock'
x = 'er'

od = OrderedDict()
for i, ch in enumerate(string):
    if ch not in od:
        od[ch] = i        #Stores the first occurrence index of each unique character in OrderedDict.
position = -1
for ch in x:       #Iterates through pattern characters sequentially.
    if ch not in od or od[ch] < position:      #Checks if the character is missing or out of order.
        print(False)
        break
    position = od[ch]       #Updates the last matched index.
else:
    print(True)
    
    
    
    
#Using OrderedDict.fromkeys
from collections import OrderedDict
string = 'Engineers Rock'
x = 'er'
od = OrderedDict.fromkeys(string)     #creates an ordered set of unique characters.
pointer = 0        #tracks the position in the pattern.
for ch in od:          #Loops through keys; if a key matches p[ptr], increment ptr.
    if ch == x[pointer]:
        pointer += 1
    if pointer == len(x):
        print(True)        #If all pattern characters are matched, prints True; otherwise prints False.
        break
else:
    print(False)
    
    
    

#Use manual insertion into OrderedDict
from collections import OrderedDict
string = 'Engineers Rock'
x = 'er'
od = OrderedDict()
for ch in string:
    if ch not in od:          #Adds unique characters to the OrderedDict, preserving their order of first occurrence.
        od[ch] = None
pointer = 0
for ch in od:          #Iterates through the keys of the OrderedDict; if a key matches x[pointer], increment pointer.
    if ch == x[pointer]:           #Advances the pointer when a match is found.
        pointer += 1
    if pointer == len(x):        #Confirms all pattern characters are matched in order; prints True if so, otherwise prints False.
        print(True)
        break