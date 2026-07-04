#Break a List into Chunks of Size N in Python

arr = [1, 2, 3, 4, 5, 6, 7, 8]

#Using List Comprehension
n = 3
result = [arr[i:i +n] for i in range(0, len(arr), n)]
print(result)


#Using itertools.islice
from itertools import islice
arr = [1, 2, 3, 4, 5, 6, 7, 8]
n = 3

a = iter(arr)
result = [list(islice(a, n)) for _ in range((len(arr) + n-1) //n)]
print(result)


#Using a for loop