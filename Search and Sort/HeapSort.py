#Heap Sort Algorithm
#Heap Sort is a comparison-based sorting technique based on a binary heap data structure. It is similar to selection sort where we first find the maximum element and place the maximum element at the end. We repeat the same 
# process for the remaining elements.
#Heap sort can be thought of as an improved selection sort: like that algorithm, it divides its input into a sorted and an unsorted region, and it iteratively shrinks the unsorted region by extracting the largest element and 
# moving that to the sorted region. The step of extracting the largest element from the unsorted region is performed using a heap data structure rather than a linear-time search, and in this way heap sort improves the 
# time complexity to O(n log n).

#Heap Sort Algorithm can be divided into two parts:
#1. Build a max heap from the input data.
#2. At this point, the largest item is stored at the root of the heap.
#   Replace it with the last item of the heap followed by reducing the size of heap by one. Finally, heapify the root of the tree.
#3. Repeat step 2 while the size of the heap is greater than 1.


#Algorithm Steps:
#1. Build a max heap from the input data.
#2. At this point, the largest item is stored at the root of the heap.
#3. Replace it with the last item of the heap followed by reducing the size of heap by one. Finally, heapify the root of the tree.
#4. Repeat step 2 while the size of the heap is greater than 1.

#How It Works:
#1. The algorithm starts by building a max heap from the input data. A max heap is a complete binary tree where the value of each node is greater than or equal to the values of its children. This ensures that the largest 
# element is always at the root of the heap.
#2. Once the max heap is built, the algorithm repeatedly swaps the root of the heap (the largest element) with the last element of the heap, effectively removing it from the heap. The size of the heap is then reduced by one, 
# and the heap property is restored by calling the heapify function

# Step 1: Represent the Array as a Binary Tree
    # For an array of size n,
    # Root is at index 0
    # Left child of node i: 2*i + 1
    # Right child of node i: 2*i + 2
    # Visualize-the-array-as-a-complete-binary-tree
    # Array as Binary Tree


# Step 2: Build a Max Heap

    # Convert the array into a max heap where each parent is larger than its children.


# Step 3: Sort the array by placing largest element at end of unsorted array.
    # Below are the detailed steps to sort the array:
    # Remove-from-Max-Heap-2.webpRemove-from-Max-Heap-2.webp
    # Swap the root (maximum) with the last element.
    # Reduce heap size and heapify the root again.
    # Repeat until the heap has one element left.
    
    
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left child index
    right = 2 * i + 2  # right child index

    # If left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child is larger than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)
def heap_sort(arr):
    n = len(arr)

    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements from heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)
heap_sort(arr)
print("Sorted array:", arr)