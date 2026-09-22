#Closest pair to kth index element in tuple
#Given a list of tuples and a target tuple, the goal is to find the tuple whose Kth element is closest to the Kth element of the target tuple. Optionally, a threshold K can define the maximum allowable difference.



#Using min with lambda
x = [(1,3,5), (2,4,6), (7,9)]
y = (8,10)
k = 2
output = min(x, key = lambda x: abs(x[k-1] - y[k-1]))       #computes the absolute difference for each tuple and returns the one with the smallest difference
print(output)


#Using emunerate and loop
x = [(1,3,5), (2,4,6), (7,9,23)]
y = (8,10,12)
k = 3
min_diff, output = float('inf'), None             #initializes tracking of the smallest difference (min_diff) and the corresponding index (output)
for index, value in enumerate(x):
    diff = abs(value[k-1] - y[k-1])
    if diff < min_diff:           #updates the smallest difference and its index whenever a smaller difference is found
        min_diff, output = diff, index
print(x[output])



#Using heapq.nsmallest()
#This method uses a heap to efficiently find the tuple(s) with the smallest difference. It’s especially useful when you want the closest N tuples rather than just one
import heapq
x = [(1,3,5), (2,4,6), (7,9,23), (23,25,27,29)]
y = (8,10,12)
k = 1
output = heapq.nsmallest(1, x, key = lambda x: abs(x[k-1] - y[k-1]))[0]         #heapq.nsmallest finds the smallest element(s) based on the provided key. 
                                                                                #key = lambda function computes the difference. [0] extracts the closest tuple
print(output)




#Using sorted with custom key
x = [(1,3,5), (2,4,6), (7,9,23), (23,25,27,29)]
y = (8,10,12)
k = 1
sort = sorted(x, key = lambda x: abs(x[k-1] - y[k-1]))
output = sort[0]
print(output)