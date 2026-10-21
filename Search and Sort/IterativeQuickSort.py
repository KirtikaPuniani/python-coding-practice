#Iterative Quick Sort
#Iterative Quick Sort is a non-recursive implementation of the Quick Sort algorithm. It uses an explicit stack to keep track of subarrays that need to be sorted, instead of relying on the call stack used in the recursive version. This approach can be more memory-efficient and avoids potential stack overflow issues for large arrays.
#Quicksort is one of the most efficient sorting algorithms and is commonly implemented using recursion. However, recursion can cause stack overflow errors when dealing with very large datasets. To overcome this, we can use an iterative version of Quicksort that replaces recursive calls with an explicit stack to manage subarrays.

# How It Works
# The algorithm divides the array into smaller parts based on a pivot element.
# Elements smaller than or equal to the pivot go to its left, and greater elements go to its right.
# Instead of recursive calls, a stack is used to keep track of subarrays that still need sorting.
# Each time a range is taken from the stack, the partition function places the pivot at its correct position, and new subarray ranges are pushed onto the stack.
# The process continues until the stack is empty - meaning the entire array is sorted.

#Partition Function
# The partition function is a key part of the Quick Sort algorithm. It rearranges the elements in the array such that all elements less than or equal to the pivot are on its left, and all elements greater than the pivot are on its right. The function returns the index of the pivot after partitioning, which is then used to determine the subarrays for further sorting.
def partition(arr, low, high):
    pivot = arr[high]  # Choosing the last element as pivot
    i = low - 1  # Pointer for the smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap if element is smaller than or equal to pivot

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place pivot in the correct position
    return i + 1
arr = [10, 7, 8, 9, 1, 5]
partition(arr)
print("Array after partitioning:", arr)





