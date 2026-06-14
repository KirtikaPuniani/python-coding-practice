arr = [1, 2, 3, 4, 5]
def SumOfElements(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum
x = SumOfElements(arr)
print("Sum of elements in the list:", x)