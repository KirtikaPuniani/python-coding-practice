#Find the size of the tuple


#Using len function
a = (1, 2, 3, 5, 'a', 9, 'b', 45, 'x')
print(len(a))


#Using sys.getsize
import sys
a = (1, 2, 3, 5, 'a', 9, 'b', 45, 'x')
print(sys.getsizeof(a))        #sys.getsizeof() measures the memory used by the tuple object itself, not the total memory used by all the objects stored inside it
# It contains 9 elements.
# Why 112 bytes?
# In a typical 64-bit CPython build, a tuple has:
# 40 bytes → fixed overhead for the tuple object
# 8 bytes × 9 → one pointer/reference for each element 
# 40 + (9 × 8) = 40 + 72 = 112 bytes



#Using memoryview
a = (1, 2, 3, 5, 'a', 9, 'b', 45, 'x')
result = memoryview(bytearray(str(a),'utf-8'))
print(result.nbytes) 