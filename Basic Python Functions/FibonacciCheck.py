def fib_check(n):
    x, y = 0, 1
    while y < n:
        x, y = y, x + y
    
    return n == y or n == 0

a = fib_check(10) 
print(a)