# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact = fact * i
#     return fact

# x = factorial(5)
# print(x)

#using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        N = n * factorial(n-1)
        return N
    
x = factorial(5)
print(x)