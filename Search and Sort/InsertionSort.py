#Insertion Sort
#Insertion Sort is a simple and intuitive sorting algorithm that works by building a sorted list one element at a time. It takes each element from the unsorted portion and inserts it into the correct position in the sorted portion.

# How Insertion Sort Works:
# Start from the second element (as the first one is already considered sorted).
# Compare the current element (called key) with the elements before it.
# Shift all larger elements one position to the right.
# Insert the key into its correct position.
# Repeat until the entire array is sorted.



def insertionSort(arr):
    n = len(arr)
    
    if n <= 1:
        return
    for i in range(1, n):
        key = arr[i]         
        j = i - 1
        while j >= 0 and key < arr[j]: 
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key      


arr = [12, 11, 13, 5, -1]
insertionSort(arr)
print(arr)

# Explanation:
# for i in range(1, n): Iterates through the array from the second element onward.
# key = arr[i]: Stores the current element to be inserted in the sorted portion.
# Inner while loop: Shifts elements greater than key one position to the right.
# arr[j + 1] = key: Inserts key into its correct sorted position.