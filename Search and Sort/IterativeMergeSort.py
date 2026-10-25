#Iterative Merge Sort
#Iterative Merge Sort is a non-recursive implementation of the Merge Sort algorithm. It sorts an array by iteratively merging subarrays of increasing sizes. This approach avoids the overhead of recursive function calls and can 
# be more efficient in terms of memory usage for large datasets.

# How It Works
# The algorithm starts by considering subarrays of size 1 (individual elements) and merges them into sorted subarrays of size 2. It then merges these sorted subarrays into larger sorted subarrays of size 4, and so on, until 
# the entire array is sorted. The process continues until the size of the subarrays being merged exceeds the length of the array.

# The merging process is similar to the merge step in the recursive Merge Sort, where two sorted subarrays are combined into a single sorted array. The iterative approach uses a loop to control the size of the subarrays being '
# merged, and it continues until the entire array is sorted.


# The working of merge sort can be broken down to the following three phases:
    # Divide: The array is initially treated as subarrays of size 1.
    # Merge: Adjacent subarrays are merged in pairs to form sorted subarrays of size 2, then 4, 8, and so on.
    # Repeat: The process continues until the entire array is merged into one sorted array.


def merge(arr, left, mid, right):
    # Create temporary arrays to hold the left and right subarrays
    left_subarray = arr[left:mid + 1]
    right_subarray = arr[mid + 1:right + 1]

    # Initialize pointers for left, right, and merged subarrays
    i = 0  # Pointer for left_subarray
    j = 0  # Pointer for right_subarray
    k = left  # Pointer for merged array

    # Merge the two subarrays back into the original array
    while i < len(left_subarray) and j < len(right_subarray):
        if left_subarray[i] <= right_subarray[j]:
            arr[k] = left_subarray[i]
            i += 1
        else:
            arr[k] = right_subarray[j]
            j += 1
        k += 1

    # Copy any remaining elements from the left subarray, if any
    while i < len(left_subarray):
        arr[k] = left_subarray[i]
        i += 1
        k += 1

    # Copy any remaining elements from the right subarray, if any
    while j < len(right_subarray):
        arr[k] = right_subarray[j]
        j += 1
        k += 1
def iterative_merge_sort(arr):
    n = len(arr)
    # Start with subarrays of size 1 and double the size in each iteration
    size = 1
    while size < n:
        # Merge subarrays in pairs
        for left in range(0, n, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)
            if mid < right:  # Only merge if there are two subarrays to merge
                merge(arr, left, mid, right)
        size *= 2
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)
iterative_merge_sort(arr)
print("Sorted array:", arr)


# Explanation:

# Divide

# iterativeMergeSort(): Treats the array as sorted subarrays of size 1.
# curr_size: Defines the size of subarrays to be merged in each pass.
# Bottom-up approach: Doubles curr_size in each iteration (1,2,4,8...).
# Outer loop (while curr_size < n): Runs until the array is completely merged.
# Conquer

# iterativeMergeSort(): Divides the array into pairs of subarrays for merging.
# left_start: Marks the starting index of the current pair of subarrays.
# merge(): Called to combine each pair (left_start…mid and mid+1…right_end).
# left_start += 2 * curr_size: Moves to the next pair after each merge.
# curr_size *= 2: Doubles subarray size after each full pass.
# Merge

# merge(): Combines two sorted subarrays into one sorted segment.
# left and right arrays: Temporary lists holding elements from both halves.
# Comparison step: Inserts smaller elements into the main array in sorted order.
# Remaining elements: Appended from whichever subarray is left.