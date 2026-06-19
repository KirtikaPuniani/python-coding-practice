#Print all odd numbers in the given range

arr = range(1, 25)

def oddRange(arr):
    odd_num = []
    for a in arr:
        if a % 2 != 0:
            odd_num.append(a)
    return odd_num

x = oddRange(arr)
print("Odd numbers in the given range:", x)