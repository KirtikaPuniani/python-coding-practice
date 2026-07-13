# Given a matrix (or 2D list) of numbers, the task is to find the product of all its elements.

#Using numpy.prod()
import numpy as np
matrix = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
result = [ele for sub in matrix for ele in sub]
result = np.prod(result)
print(result)

# Explanation: 
# b = [ele for sub in a for ele in sub] flattens the 2D list into a one-dimensional list.
# np.prod(b) multiplies all elements and returns the total product.