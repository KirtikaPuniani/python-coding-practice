#Extract the Kth column from a matrix

#Using numpy
import numpy as np
matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
k = 1  # Extract the 2nd column (0-indexed)
column = matrix[:, k]
print(column)
# Explanation:
# np.array(mat): Converts a list of lists into a NumPy array for efficient operations.
# [:, K]: Selects all rows (:) and only the Kth column (K).



#Using list comprehension
matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
k = 2   # Extract the 3rd column (0-indexed)
result = [row[k] for row in matrix]
print(result) 
# Explanation:
# List comprehension: Iterates over each row in matrix.
# row[K]: Extracts the Kth element from each row.



#Using map
matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
k = 2  # Extract the 3rd column (0-indexed)
result = list(map(lambda row: row[k], matrix))
print(result)