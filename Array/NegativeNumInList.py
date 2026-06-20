#Print all the negative numbers in a range

arr = range(-10, -5)
def negativeNum(arr):
    for a in arr:
        if a < 0:
            print(a)

print(negativeNum(arr))