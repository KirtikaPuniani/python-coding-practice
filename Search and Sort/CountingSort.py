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
    
#Algorithm
    # 1. Create a count array "countArray[max(input)+1]" initialized to 0.
    # 2. For each element in inputArray, increment countArray[element].
    # 3. Compute prefix sums in countArray.
    # 4. Create an empty outputArray of size N.
    # 5. Traverse input from the end and place each element at countArray[element] -1.
    # 6. Decrement countArray[element] after each placement.
    

def counting_sort(inputArray):
    # Step 1: Find the maximum element in the input array
    maxElement = max(inputArray)

    # Step 2: Initialize countArray of size maxElement + 1 with all zeros
    countArray = [0] * (maxElement + 1)

    # Step 3: Store the frequency of each element in countArray
    for element in inputArray:
        countArray[element] += 1

    # Step 4: Convert countArray into prefix sum
    for i in range(1, len(countArray)):
        countArray[i] += countArray[i - 1]

    # Step 5: Create an empty outputArray of size N
    outputArray = [0] * len(inputArray)

    # Step 6: Traverse input from the end and place each element at its correct position
    for i in range(len(inputArray) - 1, -1, -1):
        element = inputArray[i]
        outputIndex = countArray[element] - 1
        outputArray[outputIndex] = element
        countArray[element] -= 1

    # Step 7: Copy output back to the input array
    for i in range(len(inputArray)):
        inputArray[i] = outputArray[i]
    
    return inputArray

arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)






# Counting Sort Using collections.Counter
# The traditional Counting Sort manually counts occurrences and builds prefix sums using arrays. Python's collections.Counter offers a simpler way to achieve the same result, it automatically counts element frequencies.
# The logic remains the same:
# Count how often each element appears.
# Arrange elements in sorted order based on their counts.
# Using Counter, we skip manual array handling and directly rebuild the sorted output by iterating over sorted keys.
from collections import Counter
def counting_sort_counter(inputArray):
    # Count the frequency of each element
    count = Counter(inputArray)
    
    # Get the sorted keys (unique elements in sorted order)
    sorted_keys = sorted(count.keys())
    
    # Rebuild the sorted array based on counts
    outputArray = []
    for key in sorted_keys:
        outputArray.extend([key] * count[key])
    
    return outputArray

arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort_counter(arr)
print("Sorted array:", sorted_arr)

# Explanation:
# Counter(arr): counts occurrences of each number.
# sorted(count.keys()): gives sorted unique values.
# [num] * count[num]: repeats each number by its count.