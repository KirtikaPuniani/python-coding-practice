#Reversal algorithm for array rotation


#Method 1 - using reverse() function
arr = [1, 2, 3, 4, 5, 6, 7]
d = 2
n = len(arr)

#reverse first d element
arr[:d] = reversed(arr[:d])

#reverse remaining elements
arr[d:] = reversed(arr[d:])

#reversing the entire array
arr.reverse()
print(arr)



#Method 2 - use collections.deque
from collections import deque
arr = [1, 2, 3, 4, 5, 6, 7]
d = 2

result = deque(arr)
result.rotate(-d)
print(list(result))

# Convert list to deque for efficient rotation.
# Rotate left by d using rotate(-d).
# Convert back to list and print the result.



#Method 3 - Array Slicing
arr = [1, 2, 3, 4, 5, 6, 7]
d = 2
result = arr[d:] + arr[:d]
print(result)