#Bubble Sort Algorithm
#Bubble Sort is a simple comparison-based sorting algorithm. It works by repeatedly stepping through the list, comparing adjacent elements and swapping them if they are in the wrong order. The pass through the list is 
# repeated until the list is sorted. The algorithm gets its name because smaller elements "bubble" to the top of the list (beginning of the array) while larger elements sink to the bottom (end of the array).

# How Bubble Sort Works:
# Compare each pair of adjacent elements.
# If the first element is greater than the second, swap them.
# After each full pass, the largest unsorted element "bubbles up" to its correct position at the end.
# Repeat this process for the remaining unsorted portion of the list.
# The algorithm stops early if no swaps occur in a pass, meaning the array is already sorted.


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Flag to check if any swaps occurred in this pass
        for j in range(0, n - i - 1):  # Last i elements are already sorted
            if arr[j] > arr[j + 1]:  # Compare adjacent elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap if they are in the wrong order
                swapped = True  # Set flag to True indicating a swap occurred
        if not swapped:  # If no swaps occurred, the array is already sorted
            break
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array is:", arr)

# Explanation:
# for i in range(n): Runs multiple passes; each pass positions the next largest element at the end.
# swapped = False: Flag to detect if any swap occurs in the current pass.
# for j in range(0, n - i - 1): Iterates through unsorted elements; range shrinks as the end becomes sorted.
# if arr[j] > arr[j + 1]: Checks for inversion between adjacent elements.
# arr[j], arr[j + 1] = arr[j + 1], arr[j]: Swaps elements in place using tuple unpacking.
# if not swapped: break, Stops early if no swaps occur, indicating the array is already sorted.