#Adding and Subtracting two matrices

#Using Numpy

import numpy as np
a = np.array([[1,2], [3,4]])
b = np.array([[5,6], [7,8]])
c = np.add(a,b)
print("result of addition: \n", c)

d = np.subtract(a,b)
print("result of subtraction: \n", d)