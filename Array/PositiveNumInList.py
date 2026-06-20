#Print all the positive numbers in a range

arr = range(1,25)
def positiveNum(arr):
    for a in arr:
        if a > 0:
            print(a)

print(positiveNum(arr))