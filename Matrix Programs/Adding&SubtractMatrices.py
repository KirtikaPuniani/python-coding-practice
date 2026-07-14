#Adding and Subtracting two matrices

#Using Numpy

import numpy as np
a = np.array([[1,2], [3,4]])
b = np.array([[5,6], [7,8]])
c = np.add(a,b)
print("result of addition: \n", c)

d = np.subtract(a,b)
print("result of subtraction: \n", d)



#Using nested loops

a = np.array([[1,2], [3,4]])
b = np.array([[5,6], [7,8]])
c = [[0,0], [0,0]]
d = [[0,0], [0,0]]

for i in range(len(a)):
    for j in range(len(a[0])):
        c[i][j] = a[i][j] + b[i][j]
        d[i][j] = a[i][j] - b[i][j]

print("result of addition: \n", c)
print("result of subtraction: \n", d)