#Extract the Kth column from a matrix 

#Using numpy
import numpy as np
matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
k = 1  # Extract the 2nd column (0-indexed)
column = matrix[:, k]
print(column)




#Using list comprehension
matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
k = 2   # Extract the 3rd column (0-indexed)
result = [row[k] for row in matrix]
print(result) 