#Maximum and minimum k elements


#Using heapq
import heapq
a = (1, 3, 45, 5, 77, 45, 66, 23)
k = 2
s = heapq.nsmallest(k, a)      #Returns the k smallest elements from the iterable
l = heapq.nlargest(k, a)       #Returns the k largest elements from the iterable

print(s)
print(l)



#Using list slicing and sorted
#Convert tuple to list, sort it, and slice the first and last K elements
a = (1, 3, 45, 5, 77, 45, 66, 23)
k = 1
temp = sorted(a)        #sorted function sorts the tuple in ascending order
min = temp[:k]         #slices the first k elements as the k min elements
max = temp[-k:]        #slices the last k elements as the k ,am elements
print(min)
print(max)




#Using sorted and loop
a = (1, 3, 45, 5, 77, 45, 66, 23)
k = 1
l = sorted(a)
min, max = [], []
for i, val in enumerate(l):
    if i < k:
        min.append(val)
    if i >= len(l) - k:
        max.append(val)
print(min)
print(max)