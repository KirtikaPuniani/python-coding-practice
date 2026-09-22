#Closest pair to kth index element in tuple
#Given a list of tuples and a target tuple, the goal is to find the tuple whose Kth element is closest to the Kth element of the target tuple. Optionally, a threshold K can define the maximum allowable difference.



#Using min with lambda
x = [(1,3,5), (2,4,6), (7,9)]
y = (8,10)
k = 2
output = min(x, key = lambda x: abs(x[k-1] - y[k-1]))       #computes the absolute difference for each tuple and returns the one with the smallest difference
print(output)