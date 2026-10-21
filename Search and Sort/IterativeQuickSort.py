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





#Iterative Quick Sort Function
# The iterative quick sort function uses a stack to manage the subarrays that need to be sorted. It starts by pushing the initial range of the array onto the stack. In each iteration, it pops a range from the stack, partitions that subarray, and pushes the resulting left and right subarrays back onto the stack for further sorting. This continues until the stack is empty, indicating that the entire array has been sorted.
def iterative_quick_sort(arr):
    stack = []
    stack.append((0, len(arr) - 1))  # Push initial range onto the stack

    while stack:
        low, high = stack.pop()  # Pop a range from the stack
        if low < high:
            pi = partition(arr, low, high)  # Partition the subarray
            stack.append((low, pi - 1))  # Push left subarray onto the stack
            stack.append((pi + 1, high))  # Push right subarray onto the stack
arr = [10, 7, 8, 9, 1, 5]
iterative_quick_sort(arr)
print("Sorted array is:", arr)