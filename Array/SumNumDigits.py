#Sum of number of digits in list

arr = [12, 13, 14, 15, 16, 17, 18, 19]
total = sum(len(str(num)) for num in arr)
print(total)