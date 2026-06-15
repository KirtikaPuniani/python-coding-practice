arr = [1, 2, 3, 4, 5]
def SumOfElements(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum
x = SumOfElements(arr)
print("Sum of elements in the list:", x)



#Using lambda function
from functools import reduce    
arr = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x+y, arr)
print("Sum of elements in the list:", sum)