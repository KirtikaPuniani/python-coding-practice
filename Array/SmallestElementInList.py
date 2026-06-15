# Find the smallest element in the list

arr = [5, 2, 9, 1, 5, 6]
def find_smallest(arr):
    smallest = arr[0]
    for a in arr:
        if a < smallest:
            smallest = a
    return smallest
x = find_smallest(arr)
print("Smallest element in the list:", x)