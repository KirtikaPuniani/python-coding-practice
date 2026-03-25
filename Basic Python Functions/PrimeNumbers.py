# all prime numbers in an interval
import math

start = int(input("Enter start: "))
end = int(input("Enter end: "))

for num in range(start, end + 1):
    
    if num > 1:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                break
        else:
            print(num)