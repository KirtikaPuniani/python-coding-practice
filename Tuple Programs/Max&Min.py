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



#Using a loop and two lists
a = (1, 3, 45, 5, 77, 45, 66, 23)
k = 1
x =[]          #x and y track k smallest and largest elements
y =[]
for element in a:
    if len(x) < k:        #fill lists initially
        x.append(element)
    else:
        if element < max(x):      #replace larger/smaller elements as needed
            x.remove(max(x))
            x.append(element)
    if len(y) < k:
        y.append(element)
    else:
        if element > min(y):
            y.remove(min(y))
            y.append(element)
x.sort()
x.sort(reverse=True)
print(x)
print(y)





#Using while loop + min/max
a = (1, 3, 45, 5, 77, 45, 66, 23)
k = 1

list_a = list(a)       #Converts tuple to list to allow element removal
x = []
y = []
i = 0
while i < k:        #Loops K times to extract required smallest or largest elements
    val = min(list_a)            #Finds and removes the current smallest element, storing it in x
    x.append(val)
    list_a.remove(val)
    i += 1
i = 0
while i < k:
    val = max(list_a)          #Finds and removes the current largest element, storing it in y
    y.append(val)
    list_a.remove(val)
    i += 1
x.sort()
y.sort(reverse=True)
print(x)
print(y)