#Recursive Insertion Sort

#Recursive Insertion Sort is a variation of the standard Insertion Sort algorithm that uses recursion instead of iterative loops. It sorts an array by recursively sorting smaller portions of the array and inserting each element into its correct position in the sorted part


# Algorithm
# Treat the first n-1 elements as a smaller subproblem - sort them recursively - and then insert the nth element into the correct position among them. This process continues until the array is fully sorted. Below is the step-by-step guide:

# If the array size n <= 1, it is already sorted (base case).
# Recursively call the function to sort the first n-1 elements.
# Store the last element (the nth element) in a temporary variable last.
# Shift all elements greater than last one position ahead.
# Insert last into its correct position.
# Repeat this process until the entire array is sorted