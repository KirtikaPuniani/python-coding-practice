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