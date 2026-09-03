#Check order of character in string using OrderedDict()


#Using orderedDict() with index mapping
from collections import OrderedDict
string = 'Engineers Rock'
x = 'er'

od = OrderedDict()
for i, ch in enumerate(string):
    if ch not in od:
        od[ch] = i
position = -1
for ch in x:
    if ch not in od or od[ch] < position:
        print(False)
        break
    position = od[ch]
else:
    print(True)