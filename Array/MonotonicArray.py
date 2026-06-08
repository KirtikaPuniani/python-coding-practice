#A monotonic array is an array that consistently increases or decreases.
#Monotone Increasing: arr[i] <= arr[i + 1] for all i. Every element is less than or equal to the next one.
#Monotone Decreasing: arr[i] >= arr[i + 1] for all i. Every element is greater than or equal to the next one.
#Return: true if the array is monotonic otherwise false.
#for example:
#Input: arr = [6,5,4,4]
#Output: true
#Explanation: The array is monotone decreasing.
#Input: arr = [5, 15, 20, 10]
#Output: false
#Explanation: The array is not monotone increasing or decreasing. Array first increases then decreases.


#Using Simgle Pass:

arr = [6,5,4,4]
n = len(arr)

increasing = all(arr[i] <= arr[i+1] for i in range(n-1))
decreasing = all(arr[i] >= arr[i+1] for i in range(n-1))

print(increasing or decreasing)


#Using Direcrtional Variables:
arr = [6,5,4,4]
n = len(arr)

if n <= 2:
    print(True)
else:
    x = arr[1] - arr[0]
    y = True
    for i in range(2, n):
        if x == 0:
            x = arr[i] - arr[i-1]
            continue
        if (x > 0 and arr[i] < arr[i-1]) or (x < 0 and arr[i] > arr[i-1]):
            y = False
            break

print(y)

# def isMonotonic(arr):
#     increasing = decreasing = True
    
#     for i in range(1, len(arr)):
#         if arr[i] > arr[i - 1]:
#             decreasing = False
#         elif arr[i] < arr[i - 1]:
#             increasing = False
            
#     return increasing or decreasing