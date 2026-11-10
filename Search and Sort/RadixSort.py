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