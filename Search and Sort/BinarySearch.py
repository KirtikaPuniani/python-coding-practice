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
    i = bisect.bisect_left(arr, key)        #finds the position where key should be inserted to keep arr sorted
    if i != len(arr) and arr[i] == key:      #Checks if key exists at that position; if yes, returns the index
        return i
    else:
        return -1       #Returns -1 if the element is not found

arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search(arr, x)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")
    
    

#Iterative Binary Search
def binary_search_iterative(arr, key):
    low = 0
    high = len(arr) - 1
    
    while low <= high:       #Using a while loop to impolement iterative binary search. Initialize low and high pointers to define the search space. While low is less than or equal to high, calculate the middle index 
#and compare the middle element with the key. If they are equal, return the index. If the middle element is less than the key, update low to mid + 1 to search in the right half. Otherwise, update high to mid - 1 to search in 
#the left half. Repeat until the element is found or the search space is empty.
        mid = (low + high) // 2       #calculates the middle index by taking the average of low and high pointers. The '//' operator performs integer division, ensuring that mid is an integer value.
        
        if arr[mid] == key:        #If the middle element is equal to the key, it means the element has been found, and the function returns the index mid.
            return mid
        elif arr[mid] < key:       #If the middle element is less than the key, it means the key must be in the right half of the array. Therefore, we update low to mid + 1 to search in the right half.
            low = mid + 1
        else:                      #If the middle element is greater than the key, it means the key must be in the left half of the array. Therefore, we update high to mid - 1 to search in the left half.
            high = mid - 1
    return -1          #returns -1 if the element is not found in the array after the while loop ends.
arr = [2, 3, 4, 10, 40]
key = 10
output = binary_search_iterative(arr, key)
if output != -1:
    print("Element is present at index", output)
else:
    print("Element is not present in array")