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
# memoryview() is typically used for low-level memory management and binary data. It creates a view object that provides access to the memory buffer of an object. While not often used for simple tuples, it can be helpful in performance-sensitive scenarios.
a = (1, 2, 3, 5, 'a', 9, 'b', 45, 'x')
result = memoryview(bytearray(str(a),'utf-8'))    #bytearray(str(tup), 'utf-8') converts tuple into bytes. AND memoryview provides a view into the memory buffer.
print(result.nbytes)      #nbytes returns the number of bytes used by this byte representation.



#Using id
id() function to obtain memory address of the tuple or its elements. This method helps us to understand where objects are stored in memory, but it doesn’t directly give us their size.
a = (1, 2, 3, 5, 'a', 9, 'b', 45, 'x')
for item in a:
    print(f"Memory address of {item}: {id(item)}")
