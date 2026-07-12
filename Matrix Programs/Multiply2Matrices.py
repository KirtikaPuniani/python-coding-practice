#Using numpy

import numpy as np
a = np.array([[1, 2, 3], 
      [4, 5, 6]])

b = np.array([[7, 8, 9], 
      [10, 11, 12]])

result = np.dot(a, b.T)
for row in result:
    print(row)
    
#We used '.T' to transpose the second matrix so that the multiplication can be performed correctly. 
#Shape of a is (2, 3) (2 rows, 3 columns) and Shape of b is also (2, 3) and for matrix multiplication, the number of columns in the first matrix 
#must be equal to the number of rows in the second matrix. whereas in this case, a : (2 × 3) and b : (2 × 3), 3 ≠ 2; So we need to transpose b to 
#make it (3, 2) so that the multiplication can be performed correctly.






