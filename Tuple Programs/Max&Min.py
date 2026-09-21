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
for i, val in enumerate(l):       #enumerate loops over the sorted list with index and value
    if i < k:           #Appends first k elements to min element
        min.append(val)
    if i >= len(l) - k:         #Appends first k elements to max element
        max.append(val)
print(min)
print(max)




#Using min and max in a loop
a = (1, 3, 45, 5, 77, 45, 66, 23)
k = 1
x, y  = [], []
for element in a:
    if len(x) < k:
        x.append(element)
    else:
        if element < max(x):
            x.remove(max(x))
            x.append(element)
    if len(y) < k:    
        y.append(element)
    else:
        if element > min(y):
            y.remove(min(y))
            y.append(element)
x.sort()
y.sort(reverse=True)

print(x)
print(y)