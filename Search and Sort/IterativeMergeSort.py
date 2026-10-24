#Iterative Merge Sort
#Iterative Merge Sort is a non-recursive implementation of the Merge Sort algorithm. It sorts an array by iteratively merging subarrays of increasing sizes. This approach avoids the overhead of recursive function calls and can be more efficient in terms of memory usage for large datasets.
# How It Works
# The algorithm starts by considering subarrays of size 1 (individual elements) and merges them into sorted subarrays of size 2. It then merges these sorted subarrays into larger sorted subarrays of size 4, and so on, until the entire array is sorted. The process continues until the size of the subarrays being merged exceeds the length of the array.
# The merging process is similar to the merge step in the recursive Merge Sort, where two sorted subarrays are combined into a single sorted array. The iterative approach uses a loop to control the size of the subarrays being merged, and it continues until the entire array is sorted.
