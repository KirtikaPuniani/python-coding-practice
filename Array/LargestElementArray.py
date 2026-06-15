# Find the largest element in the list

arr = [5, 2, 9, 1, 5, 6]
def find_largest(arr):
    largest = arr[0]
    for a in arr:
        if a > largest:
            largest = a
    return largest
x = find_largest(arr)
print("largest element in the list:", x)