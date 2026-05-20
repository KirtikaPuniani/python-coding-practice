arr = [1, 2, 3, 5, 7 , 8, 9, 10, 45]
def largestElement(arr):
    largest = arr[0]
    
    for a in arr:
        if a > largest:
            largest = a
    return largest

x = largestElement(arr)
print(x)

arr2 = [1, 2, 3, 5, 45, 7, 64, 8, 99, 9, 10]
def largestElement(arr2):
    largest = arr2[0]
    
    for a in arr2:
        if a > largest:
            largest = a
    return largest

x = largestElement(arr2)
print(x)

#Time Complexity for sorted array: O(n)
#Space Complexity for sorted array: O(1) because only one extra 
# variable (largest) is used

#eg: arr2 = [1, 2, 3, 5, 45, 7, 64, 8, 99, 9, 10]
#Time Complexity for unsorted array: O(n)
#Space Complexity for unsorted array: O(1) because only one extra 
# variable (largest) is used. These are just a few variables, 
# and their number does not grow with n (array size)



#Space Complexity would become O(n) space only if you created another 
#data structure that grows with the array size, for example:
#temp = []
#for num in arr:
#    temp.append(num)