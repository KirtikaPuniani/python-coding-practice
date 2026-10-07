#Binary Search

# Binary Search is an efficient searching algorithm used to find an element in a sorted array by repeatedly dividing the search interval in half. It reduces the time complexity to O(log N), making it much faster 
# than linear search.

Here is working of Binary Search:
1. Find the middle element of the array.
2. Compare the middle element with the target key. If equal: return index.
3. If the key is smaller: search the left half.
4. If the key is larger: search the right half.
5. Repeat until the element is found or the search space is empty.