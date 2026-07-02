#Find cumulative sum of a list

#the task is to find the cumulative sum (also known as the running total) where each element in the output represents the sum of all elements up to that 
#position in the original list.

import itertools
arr = [2,3,5,7,9,18,45]
result = list(itertools.accumulate(arr))
print(result)

# arr = [2,3,5,7,9,18,45]

# def cummulativeSum(arr):
#     sum = 0
#     for a in arr:
        