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

