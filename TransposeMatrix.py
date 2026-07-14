#Transpose a matrix in single line

#Using list comprehension
matrix = [[1,2], [3,4], [5,6]]
transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print(transposed)

#Explanation: This expression creates a new matrix by taking each column from the original as a row in the new one. It swaps rows with columns.


#Using zip
#Python Zip returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. In this 
#example we unzip our array using * and then zip it to get the transpose.

matrix = [(1,2,3), (4,5,6), 
                    (7,8,9), (10,11,12)]
transposed = zip(*matrix)
for row in transposed:
    print(row)
    
    

#Using numpy
import numpy as np
matrix = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
print(np.transpose(matrix))




#Using Itertools
from itertools import chain
import time
import numpy as np
def transpose(matrix):
    matrix = matrix.tolist()
    n = len(matrix[0])
    l = list(chain(*matrix))
    return [l[i::n] for i in range(n)]

m = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])

start = time.time_ns()
result = transpose(matrix)
end = time.time_ns()

print(result)
print("Time taken to transpose the matrix using itertools: ", end-start, "ns")