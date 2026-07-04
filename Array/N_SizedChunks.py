#Break a List into Chunks of Size N in Python

arr = [1, 2, 3, 4, 5, 6, 7, 8]

#Using List Comprehension
n = 3
result = [arr[i:i +n] for i in range(0, len(arr), n)]
print(result)