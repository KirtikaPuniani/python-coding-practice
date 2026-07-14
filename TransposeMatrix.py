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
transposed = list(zip(*matrix))
print(transposed)