#Find even numbers in the list

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def evenNum(arr):
    even_num = 0
    for a in arr:
        if a % 2 == 0:
            even_num += 1
    return even_num

x = evenNum(arr)
print("Even numbers in the list:", x)