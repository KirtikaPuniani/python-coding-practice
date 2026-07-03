#Sum of number of digits in list

arr = [12, 13, 14, 15, 16, 17, 18, 19]
total = [sum(int(digit) for digit in str(num)) for num in arr]
print(total)