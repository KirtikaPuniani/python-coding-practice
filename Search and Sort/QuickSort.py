#QuickSort is a sorting algorithm based on the Divide and Conquer that picks an element as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array. 
#There are mainly three steps in the algorithm:
#1. Choose a Pivot: Select one element (first, last, random, or median) as the pivot.
#2. Partition the Array: Rearrange elements so that those smaller than the pivot are placed to its left and those greater are placed to its right. The pivot then moves to its correct sorted position.
#3. Recursive Sorting: Recursively apply the same process to the left and right subarrays until all elements are sorted.
#4. Base Case: When a subarray has one or no element, it is already sorted.