#Multiply all numbers in a list

arr = [1, 2, 3, 4, 5]
def MultiplyArrayElements(arr):
    multiply = 1
    for i in arr:
        multiply *= i
    return multiply
x = MultiplyArrayElements(arr)
print("Multiplication of elements in the list:", x)