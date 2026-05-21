#Method 1 - Uing slicing
arr = [1, 2, 3, 4, 5]
d = 2
arr[:] = arr[d:] + arr[:d]
print(arr)


#Method 2 - Using reverse() method
arr = [1, 2, 3, 4, 5]
d = 2
n = len(arr)
arr.reverse()

arr[:n-d] = arr[:n-d][::-1]
arr[n-d:] = arr[n-d:][::-1]
print(arr)

#arr[d:]: elements from index d to end.
#arr[:d]: first d elements.
#arr[:] = arr[d:] + arr[:d]: updates array in-place.