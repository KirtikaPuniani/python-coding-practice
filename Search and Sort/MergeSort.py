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