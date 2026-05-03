def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

x = fibonacci(10)
y = fibonacci(9)
print(x)
print(y)




#Using Dynamic Programing for space optimization
def fibonacci(n):
    if n < 0:
        return "Incorrect input is given"
    x, y = 0, 1
    for _ in range(n):
        x, y = y, x + y
    return x

f = fibonacci(10)
print(f)