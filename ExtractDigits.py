#Extract digits from tuple list
#Given a list of tuples containing numbers of varying lengths, the task is to extract all unique digits present in those tuples
#Example:
# Input: list = [(15, 3), (3, 9)] 
# Output: [9, 5, 3, 1]

# Input: list = [(15, 3)] 
# Output: [5, 3, 1] 



#Using list comprehension and set
tup = [(15, 3), (3, 9), (1, 10), (99, 2)] #[(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
temp = ''.join([str(i) for x in tup for i in x])
output = [int(i) for i in set(temp)]
print(output)