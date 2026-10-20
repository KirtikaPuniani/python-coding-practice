#QuickSort is a sorting algorithm based on the Divide and Conquer that picks an element as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array. 
#There are mainly three steps in the algorithm:
#1. Choose a Pivot: Select one element (first, last, random, or median) as the pivot.
#2. Partition the Array: Rearrange elements so that those smaller than the pivot are placed to its left and those greater are placed to its right. The pivot then moves to its correct sorted position.
#3. Recursive Sorting: Recursively apply the same process to the left and right subarrays until all elements are sorted.
#4. Base Case: When a subarray has one or no element, it is already sorted.

# In this implementation, last element is chosen as the pivot, and the partitioning ensures all smaller elements are on one side and larger on the other, achieving sorting efficiently.
# Algorithm Steps of QuickSort

# 1. Input: Array A, starting index low, ending index high
# 2. If low < high, then Partition: Find pivot index p = partition(A, low, high)
#                        Recur: Apply QuickSort to left subarray -> quickSort(A, low, p - 1)
#                        Apply QuickSort to right subarray -> quickSort(A, p + 1, high)
# 3. Else: Stop (base case - subarray of size ≤ 1 is already sorted)
# 4. Output: Sorted array A



#Using recursive quicksort function
#The function takes an array, the starting index, and the ending index as input. It partitions the array around a pivot and recursively sorts the left and right subarrays until the entire array is sorted.
def partition(arr, low, high):
    pivot = arr[high]  # Choosing the last element as pivot
    i = low - 1  # Pointer for the smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap if element is smaller than or equal to pivot

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place pivot in the correct position
    return i + 1
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)  # Partitioning index
        quick_sort(arr, low, pi - 1)  # Recursively sort elements before partition
        quick_sort(arr, pi + 1, high)  # Recursively sort elements after partition
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quick_sort(arr, 0, n - 1)
print("Sorted array is:", arr)