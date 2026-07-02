#Find cumulative sum of a list

#the task is to find the cumulative sum (also known as the running total) where each element in the output represents the sum of all elements up to that 
#position in the original list.

import itertools
arr = [2,3,5,7,9,18,45]
result = list(itertools.accumulate(arr))
print(result)


import numpy as np
l = [1, 2, 3, 4]
res = np.cumsum(l)
print(res)

arr = [2,3,5,7,9,18,45]
def cummulativeSum(arr):
    total = 0
    result = []
    for num in arr:
        total += num
        result.append(total)
    return result
print(cummulativeSum(arr))