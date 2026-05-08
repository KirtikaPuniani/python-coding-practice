#Sum of square of n natural numbers
def sumOfSquares(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**2
    return sum

x = sumOfSquares(5)
print(x)