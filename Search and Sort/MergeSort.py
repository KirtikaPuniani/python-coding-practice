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