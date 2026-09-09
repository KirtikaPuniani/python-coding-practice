#Check if binary representations of two numbers are anagram


#Using Bitwise Operations
x, y = 8, 4
a = bin(x).count('1')
b = bin(y).count('1')

c = max(x.bit_length(), y.bit_length())

n = x - a
m = x - b

if a == b and n == m:
    print("Yes")
else:
    print("No")