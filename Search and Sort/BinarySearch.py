#Binary Search

# Binary Search is an efficient searching algorithm used to find an element in a sorted array by repeatedly dividing the search interval in half. It reduces the time complexity to O(log N), making it much faster 
# than linear search.

# Here is working of Binary Search:
# 1. Find the middle element of the array.
# 2. Compare the middle element with the target key. If equal: return index.
# 3. If the key is smaller: search the left half.
# 4. If the key is larger: search the right half.
# 5. Repeat until the element is found or the search space is empty.



#Using bisect
import bisect
def binary_search(arr, key):
    i = bisect.bisect_left(arr, x)
    if i != len(arr) and arr[i] == x:
        return i
    else:
        return -1

arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search(arr, x)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")