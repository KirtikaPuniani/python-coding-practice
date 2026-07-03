#Sum of number of digits in list

# Given a list of integers, write a Python program to calculate the sum of digits for each element and store the results in a new list. 
# For Example:
# Input: [123, 456, 789]  
# Output: [6, 15, 24]
# Explanation:  123 = 1 + 2 + 3 = 6  
#               456 = 4 + 5 + 6 = 15  
#               789 = 7 + 8 + 9 = 24 

arr = [12, 13, 14, 15, 16, 17, 18, 19]
total = [sum(int(digit) for digit in str(num)) for num in arr]
print(total)