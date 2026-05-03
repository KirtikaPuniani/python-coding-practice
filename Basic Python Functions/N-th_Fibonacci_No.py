def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

x = fibonacci(10)
y = fibonacci(9)
print(x)
print(y)


#--------------------------------------------------------------


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

# a, b = 0, 1 stores first two values
# for _ in range(n) runs loop n times
# a, b = b, a + b shifts values to next pair
# return a returns required Fibonacci number



#--------------------------------------------------------------


# Recursion with Memoization
# Memoization method stores previously computed Fibonacci values in a dictionary. When a value is needed again, it is directly returned instead of recalculating.

fib_cache = {0: 0, 1: 1}

def fibonacci(n):
    if n in fib_cache:
        return fib_cache[n]
    else:
        fib_cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return fib_cache[n]

a = fibonacci(12)
print(a)