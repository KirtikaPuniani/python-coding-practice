#Find the size of the tuple


#Using len function
a = (1, 2, 3, 5, 'a', 9, 'b', 45, 'x')
print(len(a))


#Using sys.getsize
import sys
a = (1, 2, 3, 5, 'a', 9, 'b', 45, 'x')
print(sys.getsizeof(a))