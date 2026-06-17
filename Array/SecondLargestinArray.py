#Second Largest number in Array

arr = [1, 15, 34, 25, 78, 19, 20, 87, 100, 89, 200]

def secondLargest(arr):
    largest = arr[0]
    second_largest = float('-inf')  # Initialize to negative infinity
    
    for a in arr:
        if a > largest:
            second_largest = largest
            largest = a
        elif a > second_largest and a != largest:
            second_largest = a
            
    return second_largest

x = secondLargest(arr)
print("Second largest element in the list:", x)




#Using heapq.largest() function to find the second largest element in the list
import heapq
arr = [1, 15, 34, 25, 78, 19, 20, 87, 100, 89, 200]
second_largest = heapq.nlargest(2, arr)
print(second_largest[1])  # Output: 100