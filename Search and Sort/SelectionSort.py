#Selection Sort Algorithm
#Selection Sort is a simple comparison-based sorting algorithm. It works by repeatedly finding the minimum element from the unsorted portion of the array and placing it at the beginning. The algorithm maintains two subarrays: the sorted subarray and the unsorted subarray. Initially, the sorted subarray is empty, and the unsorted subarray contains all the elements. The algorithm iteratively selects the smallest element from the unsorted subarray and swaps it with the leftmost unsorted element, effectively growing the sorted subarray and shrinking the unsorted subarray until the entire array is sorted.

# Working of Selection Sort:
# Start from the first element and find the smallest element in the entire array by iterating over it.
# Swap this smallest element with the first element.
# Now, move to the second element find the next smallest in the remaining unsorted portion and swap it with the second position.
# Repeat this process until the entire array becomes sorted.