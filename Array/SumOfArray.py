arr = [ 1, 3, 5, 7, 9]
def sumOfArray(arr):
    sum = 0
    for a in arr:
        sum += a
    return sum

x = sumOfArray(arr)
print(x)


#using in-built reduce() funtion: this function from functools applies a
#function cumulatively to the elements of an iterable, effectively 
#summing all elements

from functools import reduce
arr = [1, 2, 3, 4, 5, 6, 7]
result = reduce(lambda a , b: a +b, arr)
print('Sum of the elements =', result)

#Using enumerate() function: this function allows loopinf through an 
#array with an index and element

arr = [1, 2, 3, 4, 5]
sum = 0
for i, val in enumerate(arr):
    sum += val
print(sum)