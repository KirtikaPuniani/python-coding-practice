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
# Explanation:
# map(): Applies a function to each element of matrix (each row).
# lambda row: row[K]: Anonymous function that extracts the Kth element from a row.
# list(): Converts the map object into a list.



#Using zip
matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
k = 0  # Extract the 1st column (0-indexed)
result = list(zip(*matrix))[k]
print(result)
# Explanation:
# zip(*matrix): Transposes the matrix, turning rows into columns.
# list(): Converts the zip object into a list of tuples.



#Using a for loop
matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
k = 1  # Extract the 2nd column (0-indexed)
result = []
for row in matrix:
    result.append(row[k])
print(result)
# Explanation:
# for loop: Iterates over each row in the matrix.
# row[K]: Extracts the Kth element from each row and appends it to the result list.