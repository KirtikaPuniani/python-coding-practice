#Linear Search

# Linear Search checks each element of a list one by one until the desired element is found or the list ends. Given an array of n elements and an element x, find whether element x is present in the array. Return the index of the 
# first occurrence of x in the array, or -1 if it doesn’t exist.

# Examples:
# Input: arr[] = [10, 50, 30, 70, 80, 20, 90, 40], x = 30
# Output : 2
# Explanation: For array  [10, 50, 30, 70, 80, 20, 90, 40], the element to be searched is 30 and it is at index 2. So, the output is 2.

#A simple approach is to do a linear search, i.e
# Start from the leftmost element of arr[] and one by one compare x with each element of arr[].
# If x matches with an element, return the index.
# If x doesn't match with any of the elements, return -1.




#Using iterative approach to implement linear search. 
#The function takes an array and a key as input, and iterates through the array to find the key. If the key is found, it returns the index; otherwise, it returns -1.
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = [10, 23, 45, 70, 11, 15]
x = 70
res = linear_search(arr, x)

if res != -1:
    print("Element found at index:", res)
else:
    print("Element not found in the array")
    
    
    
#Usimg recursive approach to implement linear search. The function takes an array, the current index, and the key as input. It checks if the current index is within bounds and compares the element at that index with the key. If they match, it returns the index; otherwise, it recursively calls itself with the next index. If the end of the array is reached without finding the key, it returns -1.
def linear_search_rec(arr, x, i=0):
    if i == len(arr):
        return -1
    if arr[i] == x:
        return i
    return linear_search_rec(arr, x, i + 1)

arr = [10, 20, 30, 40, 50]
x = 30
res = linear_search_rec(arr, x)

if res != -1:
    print("Element", x, "found at index", res)
else:
    print("Element", x, "not found in the list")
    
    

#Using RegEx Method
import re

def regex_search(lst, pat):
    reg = re.compile(pat)
    for i, ele in enumerate(lst):
        if reg.search(ele):
            return "Pattern found in element '" + ele + "' at index " + str(i)
    return "Pattern not found in the list"

lst = ["apple", "banana", "cherry", "date", "elderberry"]
pat = "an"
res = regex_search(lst, pat)
print(res)

# Explanation:
# re.compile(pat) compiles the search pattern.
# Each list element is checked using reg.search(ele).
# Returns the matching element and its index if found; otherwise, returns a message saying not found.