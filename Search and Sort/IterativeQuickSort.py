#Iterative Quick Sort
#Iterative Quick Sort is a non-recursive implementation of the Quick Sort algorithm. It uses an explicit stack to keep track of subarrays that need to be sorted, instead of relying on the call stack used in the recursive version. This approach can be more memory-efficient and avoids potential stack overflow issues for large arrays.
#Quicksort is one of the most efficient sorting algorithms and is commonly implemented using recursion. However, recursion can cause stack overflow errors when dealing with very large datasets. To overcome this, we can use an iterative version of Quicksort that replaces recursive calls with an explicit stack to manage subarrays.

# How It Works
# The algorithm divides the array into smaller parts based on a pivot element.
# Elements smaller than or equal to the pivot go to its left, and greater elements go to its right.
# Instead of recursive calls, a stack is used to keep track of subarrays that still need sorting.
# Each time a range is taken from the stack, the partition function places the pivot at its correct position, and new subarray ranges are pushed onto the stack.
# The process continues until the stack is empty - meaning the entire array is sorted.