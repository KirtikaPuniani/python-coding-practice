#Method 1 - Uing slicing
arr = [1, 2, 3, 4, 5]
d = 2
arr[:] = arr[d:] + arr[:d]
print(arr)

#arr[d:]: elements from index d to end.
#arr[:d]: first d elements.
#arr[:] = arr[d:] + arr[:d]: updates array in-place.


#------------------------------------------------------#

#Method 2 - Using reverse() method
arr = [1, 2, 3, 4, 5]
d = 2
n = len(arr)
arr.reverse()

arr[:n-d] = arr[:n-d][::-1]
arr[n-d:] = arr[n-d:][::-1]
print(arr)

#arr.reverse(): reverses the whole array.
#arr[:n-d][::-1] reverses the first part.
#arr[n-d:][::-1] reverses the last part.

#------------------------------------------------------#

#Method 3 - Using temporary array
arr = [1, 2, 3, 4, 5, 6, 7]
d = 3
n = len(arr)

temp = arr[:d]
arr[:n-d] = arr[d:]
arr[n-d:] = temp

print(arr)

# temp = arr[:d] store the first d elements.
# arr[:n-d] = arr[d:] shift the remaining elements left.
# arr[n-d:] = temp place the stored elements at the end.

#------------------------------------------------------#

#Method 4 - One by one rotation
arr = [1, 2, 3, 4, 5, 6, 7]
d = 3
n = len(arr)

for i in range(d):
    arr.append(arr.pop(0))
print(arr)
# arr.pop(0) removes the first element and returns it.
# arr.append(...) adds the removed element to the end of the array.
