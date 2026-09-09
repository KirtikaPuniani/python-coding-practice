#Check if binary representations of two numbers are anagram


#Using Bitwise Operations
x, y = 8, 4
a = bin(x).count('1')    #counts number of 1s in binary form
b = bin(y).count('1')

c = max(x.bit_length(), y.bit_length())      #bin_length gives the number of bits required to represent the number in binary.

n = x - a
m = x - b
#0's are found indirectly as total bits minus 1s. If boths have equal counts of 0's and 1's, then they are anagrams. So we can check if the difference of total bits and 1's is equal for both numbers.
if a == b and n == m:
    print("Yes")
else:
    print("No")
    
    
    
    
#Using zfill() and counting bits
x, y = 10, 13
a = bin(x)[2:].zfill(32)       #bin() converts the given integer into binary strings. [2:] removes the '0b' prefix from the binary string. zfill() pads the string with leading zeros to make it 32 bits long.
b = bin(y)[2:].zfill(32)

n = [a.count('0'), a.count('1')]       #counts the number of 0's and 1's in the binary representation of x and y and creates a list
m = [b.count('0'), b.count('1')]
if n == m:         #If both the lists mathches then binaries are anagrams
    print("Yes")
else:
    print("No")
    
    
    
    
#Using collections.Counter and dictionary comparison
from collections import Counter
x, y = 10, 12
a = bin(x)[2:]       #binary strings without '0b'
b = bin(y)[2:]
pad = abs(len(a) - len(b))
if len(a) > len(b):
    y = '0' * pad + b      #adds zeros to equilize lengths
else:
    y = '0' * pad + a
n = Counter(b)      #creates frequency  maps of 0s and 1s
m = Counter(a)
if n == m:      #if equal counters binaries are anagrams
    print('Yes')
else:
    print('No') 