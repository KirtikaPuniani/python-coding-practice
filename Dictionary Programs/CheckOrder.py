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
od = OrderedDict.fromkeys(string)
pointer = 0
for ch in od:
    if ch == x[pointer]:
        pointer += 1
    if pointer == len(x):
        print(True)
        break
else:
    print(False)