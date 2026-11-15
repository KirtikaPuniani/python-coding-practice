#Binary Insertion Sort
#Binary Insertion Sort is a sorting algorithm that combines the principles of Insertion Sort and Binary Search. It improves the efficiency of the traditional Insertion Sort by using Binary Search to find the correct position 
# for each element in the sorted portion of the array, reducing the number of comparisons needed.

# Given an array of integers, the task is to sort the elements in ascending order using Binary Insertion Sort. Unlike the traditional insertion sort, this algorithm uses binary search to find the correct position for inserting 
# an element, which reduces unnecessary comparisons and makes sorting more efficient while maintaining a stable order.'


#for example, consider the following array of integers: [5, 2, 9, 1, 5, 6]. The Binary Insertion Sort algorithm will sort this array in ascending order as follows:
#Input: [37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]
#Output: [0, 12, 17, 23, 31, 37, 46, 54, 72, 88, 100]
#Explanation: The algorithm places each unsorted element into its correct position in the sorted portion of the array using binary search, resulting in a fully sorted list.



# Algorithm Steps
    # Start with the second element (index 1) since the first element is considered sorted.
    # Perform binary search on the sorted part of the array (from index 0 to i-1) to find the correct position for the current element.
    # Shift all elements greater than the current element one position ahead to make space.
    # Insert the current element at its correct position found by binary search.
    # Repeat steps 2-4 for all remaining elements in the array until it becomes fully sorted.
    
    
    
#Using User Defined Binary Search Function
def binary_search(arr, val, start, end):
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1
    if start > end:
        return start

    mid = (start + end) // 2
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid - 1)
    else:
        return mid

def insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i - 1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i + 1:]
    return arr

print("Sorted array:")
print(insertion_sort([37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]))