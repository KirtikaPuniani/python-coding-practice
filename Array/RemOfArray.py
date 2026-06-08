# Given an array of numbers and an integer n, the task is to find the remainder when all numbers in the array are 
# multiplied and divided by n.

# Examples:
# Input: arr[] = [100, 10, 5, 25, 35, 14],  n = 11
# Output: 9
# Explanation: 100 x 10 x 5 x 25 x 35 x 14 = 61250000 % 11 = 9

####### Method 1 #######
#Using Modular Multiplication
# modular arithmetic is used to avoid overflow. Instead of multiplying all numbers at once, we take the remainder of 
# each number with n during multiplication:
# (a * b) % n = ((a % n) * (b % n)) % n

arr = [100, 10, 5, 25, 35, 14]
n = 11
mul = 1
for num in arr:
    mul = (mul * (num % n)) % n
print(mul)

# Explanation:
# Start with mul = 1.
# Multiply first element 100 -> (1 * 100) % 11 = 1
# Multiply next 10 -> (1 * 10) % 11 = 10
# Continue for all elements -> final remainder 9.





########### Method 2 ###########
#Using functools.reduce() 
from functools import reduce
arr = [100, 10, 5, 25, 35, 14]
n = 11
result = reduce(lambda x, y: (x * y) % n, arr)
print(result)
#The reduce function from functools can iterate through the array, multiplying 
# elements and taking modulo n at each step.







###### Method 3 #######
#Using Naive Multiplication
arr = [100, 10, 5, 25, 35, 14]
n = 11
prd = 1
for num in arr:
    prd *= num
result = prd % n
print(result)
#This method multiplies all numbers first and then applies modulo n. 
# It’s simple but can overflow if the numbers are large.