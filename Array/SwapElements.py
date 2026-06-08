#Using multiple assignment

arr = [10, 20, 30, 40, 50]
def swap_elements(arr, index1, index2):
    arr[index1], arr[index2] = arr[index2], arr[index1]
    return arr

print(swap_elements(arr, 0, 4))





#using a temporary variable
arr = [10, 20, 30, 40, 50]
def swap_elements(arr, index1, index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp
    return arr
print(swap_elements(arr, 0, 4))