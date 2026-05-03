#Using Loop
def fib_check(n):
    x, y = 0, 1
    while y < n:
        x, y = y, x + y
    
    return n == y or n == 0

a = fib_check(10) 
print(a)



#Using math -- interview favourite
import math

def is_perfect_square(n):
    x = int(math.sqrt(n))
    return x * x == n

def fib_check(y):
    return is_perfect_square(5*y*y + 4) or is_perfect_square(5*y*y - 4)

b = fib_check(47)
print(b)