#Count Sort Algorithm
#Counting Sort is a non-comparison based sorting algorithm that sorts elements by counting the number of occurrences of each unique element in the input array. It is particularly efficient for sorting integers or categorical 
# data with a limited range of values. Counting Sort is a non-comparison-based sorting algorithm. It is highly efficient when the range of input values is small compared to the number of elements. The main idea is to count the 
# occurrences of each element and then use these counts to determine the correct position of each element in the sorted output.

# How It Works:
# The algorithm works by creating a count array that keeps track of the number of occurrences of each unique element in the input array. It then calculates the cumulative count to determine the position of each element in the 
# sorted output array. Finally, it constructs the sorted output array by placing each element at its correct position based on the cumulative count.

#Working of Counting Sort:
    # 1. Find the maximum element in the input array.
    # 2. Initialize a countArray of size max + 1 with all zeros.
    # 3. Store the frequency of each element from the input array at its corresponding index in countArray.
    # 4. Example: if 2 appears twice, countArray[2] = 2.
    # 5. Convert countArray into prefix sum each index now shows the final position of that element in the sorted order.
    # 6. Build the output array by iterating the input array from the end (to maintain stability).
    # 7. Copy output back to the input array.