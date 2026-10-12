#Linear Search

# Linear Search checks each element of a list one by one until the desired element is found or the list ends. Given an array of n elements and an element x, find whether element x is present in the array. Return the index of the 
# first occurrence of x in the array, or -1 if it doesn’t exist.

# Examples:
# Input: arr[] = [10, 50, 30, 70, 80, 20, 90, 40], x = 30
# Output : 2
# Explanation: For array  [10, 50, 30, 70, 80, 20, 90, 40], the element to be searched is 30 and it is at index 2. So, the output is 2.

#A simple approach is to do a linear search, i.e
# Start from the leftmost element of arr[] and one by one compare x with each element of arr[].
# If x matches with an element, return the index.
# If x doesn't match with any of the elements, return -1.