# The task of adding two matrices in Python involves combining corresponding elements from two given matrices to produce a new matrix. 
# Each element in the resulting matrix is obtained by adding the values at the same position in the input matrices.



# Using Numpy

import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])
result = a + b
print(result)




#Using list comprehension

a = [[1, 2, 3], [4, 5, 6]]
b = [[7, 8, 9], [10, 11, 12]]

result = [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
for r in result:
    print(r)
