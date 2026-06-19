#Find odd numbers in the list

arr = [1,3,4,5,7,8,9,11,89,98]

def oddNum(arr):
    odd_num = 0
    for a in arr:
        if a % 2 != 0:
            odd_num += 1
    return odd_num

x = oddNum(arr)
print("Odd numbers in the list:", x)