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
a = bin(x)[2:].zfill(32)
b = bin(y)[2:].zfill(32)

n = [a.count('0'), a.count('1')]
m = [b.count('0'), b.count('1')]
if n == m:
    print("Yes")
else:
    print("No")