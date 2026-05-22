#Reversal algorithm for array rotation

arr = [1, 2, 3, 4, 5, 6, 7]
d = 3
n = len(arr)

#reverse first d element
arr[:d] = reversed(arr[:d])

#reverse remaining elements
arr[d:] = reversed(arr[d:])

#reversing the entire array
arr.reverse()
print(arr)