#Radix Sort
# Given an array of integers, the task is to sort the elements in ascending order using Radix Sort. Radix Sort processes each digit of the numbers starting from the least significant digit to the most significant digit. 
# It groups numbers into buckets based on their digit values and rearranges them after every pass until all digits are processed.


# Working of Radix Sort Algorithm
# To sort the array [170, 45, 75, 90, 802, 24, 2, 66], Radix Sort processes digits one place at a time, starting from the least significant digit (LSD) to the most significant digit (MSD).
    # Step 1: Find the largest number 802, which has 3 digits, so the algorithm performs 3 iterations (units, tens, hundreds).
    # Step 2: Sort by units place. Using a stable counting sort, the array becomes -> [170, 90, 802, 2, 24, 45, 75, 66].
    # Step 3: Sort by tens place. Sorting again by the tens digit gives -> [802, 2, 24, 45, 66, 170, 75, 90].
    # Step 4: Sort by hundreds place. Sorting by the hundreds digit results in -> [2, 24, 45, 66, 75, 90, 170, 802].
    # Step 5: After all digits are processed, the array is fully sorted. Final Output: [2, 24, 45, 66, 75, 90, 170, 802]
    
    

#Using Counting Sort (digit by digit approach)
#This method is used to sort the elements based on the individual digits of the numbers. It ensures that the relative order of elements with equal keys is preserved, making it a stable sorting algorithm. Once the elements are 
# sorted based on the current digit, the algorithm moves to the next significant digit and repeats the process until all digits have been processed. It's memory efficienty and works well for sorting integers with a 
# limited range of digits.
def radix_sort(arr):
    max_num = max(arr)
    exp = 1  # Represents current digit place (1, 10, 100, ...)

    while max_num // exp > 0:
        n = len(arr)
        output = [0] * n
        count = [0] * 10  # For digits 0–9

        # Count occurrences of each digit
        for num in arr:
            index = (num // exp) % 10
            count[index] += 1

        # Convert count[] to actual positions
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build output array (in reverse for stability)
        for i in range(n - 1, -1, -1):
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1

        # Copy output to arr[]
        for i in range(n):
            arr[i] = output[i]

        exp *= 10

arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print(arr)






#Using bucket sort logic
#This version uses digit-based bucketing to sort the elements. It distributes the numbers into buckets based on their digit values and then concatenates the buckets after sorting each digit. This approach is particularly 
# effective for sorting integers with a limited range of digits.
def radix_sort_bucket(arr):
    max_num = max(arr)
    exp = 1  # Represents current digit place (1, 10, 100, ...)

    while max_num // exp > 0:
        buckets = [[] for _ in range(10)]  # Create 10 buckets for digits 0–9

        # Distribute elements into buckets based on current digit
        for num in arr:
            index = (num // exp) % 10
            buckets[index].append(num)

        # Concatenate buckets back into arr
        arr.clear()
        for bucket in buckets:
            arr.extend(bucket)

        exp *= 10
    
    return arr

arr = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_arr = radix_sort_bucket(arr)
print(sorted_arr)





