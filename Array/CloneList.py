#Cloning or copying a list

arr = [1,2,3,4,5]
def cloneList(arr):
    return arr[:]
print(cloneList(arr))


#using deepcopy()
import copy
arr = [1,2,3,4,5]
def cloneList(arr):
    return copy.deepcopy(arr)
print(cloneList(arr))


#Using list comprehension
arr = [1,2,3,4,5]
b = [item for item in arr]
print(b)