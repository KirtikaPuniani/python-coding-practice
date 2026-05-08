#Cube sum of first n natural numbers
def sumOfCubes(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**3
    return sum

x = sumOfCubes(5)
print(x)