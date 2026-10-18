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

def recursive_insertion_sort(arr, n):
    # Base case: If the array size is 1 or less, it's already sorted
    if n <= 1:
        return

    # Recursively sort the first n-1 elements
    recursive_insertion_sort(arr, n - 1)

    # Store the last element (the nth element)
    last = arr[n - 1]
    j = n - 2

    # Shift elements of arr[0..n-2], that are greater than last, to one position ahead
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1

    # Insert last into its correct position
    arr[j + 1] = last

