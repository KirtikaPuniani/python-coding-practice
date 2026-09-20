#Maximum and minimum k elements


#Using heapq
import heapq
a = (1, 3, 45, 5, 77, 45, 66, 23)
k = 2
s = heapq.nsmallest(k, a)      #Returns the k smallest elements from the iterable
l = heapq.nlargest(k, a)       #Returns the k largest elements from the iterable

print(s)
print(l)