# Given an array and an integer k, the task is to split the array from the kth position and move the first part to 
#the end. 

# For Example:
# Input: arr = [12, 10, 5, 6, 52, 36], k = 2  
# Output: [5, 6, 52, 36, 12, 10]
# Explanation: Split the array at index k and move the first part [12, 10] (for k = 2) to the end.

#Using deque.rotate() method
from collections import deque
arr = [12, 10, 5, 6, 52, 36]
k = 2

d = deque(arr)
d.rotate(-k)
result = list(d)
print(result)

#Explanation:
# deque(arr): converts the list into a double-ended queue
# rotate(-k): shifts the elements left by k positions
# list(d): converts the deque back into a list




######### Method 2 ###########
#Using slicing
arr = [12, 10, 5, 6, 52, 36]
k = 2   

arr = arr[k:] + arr[:k]
print(arr)

# Explanation:
# arr[:k]: first k elements.
# arr[k:]: remaining elements.
# Concatenating them gives the rotated array.



######### Method 3 ###########
#Using List Comprehension and Modulo Operator
arr = [12, 10, 5, 6, 52, 36]
k = 2   

n = len(arr)
result = [arr[(i + k) % n] for i in range(n)]
print(result)

# Explanation:
# (i + k) % len(arr): wraps indices around the array, ensuring the rotation is circular.
# Creates a rotated version without modifying the original array.




######### Method 4 ###########
#Using Extend()
arr = [12, 10, 5, 6, 52, 36]
k = 2

x = arr[:k]
y = arr[k:]
y.extend(x)
print(y)

# Explanation:
# arr[:k]: extracts the first k elements.
# arr[k:]: remaining part.
# extend(x): appends the first part to the end.