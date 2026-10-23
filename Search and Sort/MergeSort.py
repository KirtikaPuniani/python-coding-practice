#Merge Sort Algorithm
#Merge Sort is a divide-and-conquer algorithm that divides the input array into two halves, recursively sorts each half, and then merges the two sorted halves back together. It is an efficient and stable sorting algorithm with 
# a time complexity of O(n log n).
#It is one of the most efficient and stable sorting algorithms based on the Divide and Conquer technique. It divides an input array into two halves, recursively sorts them, and then merges the two sorted halves using a 
# function called merge().
#The key function, merge(arr, l, m, r), assumes that both halves arr[l..m] (left half) and arr[m+1..r] (right half) are already sorted and merges them into one sorted array.


# How Merge Sort Works: ----
# Here’s the step-by-step breakdown:
# Divide: Recursively split the array into two halves until each subarray has only one element.
# Conquer: Sort each subarray individually (they’re already sorted if they contain one element).
# Merge: Combine the sorted subarrays into a single sorted array in the correct order.


# Illustration of Merge Sort:
#     Let’s sort the array or list [38, 27, 43, 10] using Merge Sort
# Let’s look at the working of above example:

# Divide:

# [38, 27, 43, 10] is divided into [38, 27 ] and [43, 10] .
# [38, 27] is divided into [38] and [27] .
# [43, 10] is divided into [43] and [10] .
# Conquer:

# [38] is already sorted.
# [27] is already sorted.
# [43] is already sorted.
# [10] is already sorted.
# Merge:

# Merge [38] and [27] to get [27, 38] .
# Merge [43] and [10] to get [10,43] .
# Merge [27, 38] and [10,43] to get the final sorted list [10, 27, 38, 43]
# Therefore, the sorted list is [10, 27, 38, 43].



def merge(arr, l, m, r):
    # Create temporary arrays to hold the left and right subarrays
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    # Copy data to temporary arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temporary arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, l, r):
    if l < r:
        # Find the middle point to divide the array into two halves
        m = (l + r) // 2

        # Recursively sort the first and second halves
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)

        # Merge the sorted halves
        merge(arr, l, m, r)

arr = [38, 27, 43, 10]
merge_sort(arr, 0, len(arr) - 1)
print("Sorted array is:", arr)