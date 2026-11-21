#Bitonic Sort

# A sequence is bitonic if it first increases and then decreases. Formally, an array arr[0..n-1] is bitonic if there exists an index i (0 ≤ i ≤ n−1) such that:

# x0 <= x1 …..<= xi  and  xi >= xi+1….. >= xn-1
# A fully increasing or fully decreasing sequence is also considered bitonic.
# Any rotation of a bitonic sequence remains bitonic.
# Bitonic Sort is a parallel sorting algorithm that works efficiently when the number of elements is a power of 2.

# How Bitonic Sort Works
    # It mainly works in two steps:
    # Form a bitonic sequence: divide the array into two halves- one sorted in ascending order and the other in descending order.
    # Merge: compare and swap elements to form smaller bitonic sequences until the entire array is sorted.




