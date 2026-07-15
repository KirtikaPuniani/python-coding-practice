#Given a number n, the task is to create an n × n matrix in Python.

#Using Numpy zeros

import numpy as np
n = 3
result = np.zeros((n,n), dtype=int)
for row in result:
    print(row)
    
    
    
    
#Using numpy full()
import numpy as np
n = 3
result = np.full((n,n), 5, dtype=int)
for row in result:
    print(row)
    



#Using Nested list comprehension
n = 3
result = [[0 for j in range(n)] for i in range(n)]
for row in result:
    print(row)
    
    

#Using nested loops
n = 3
m = []
count = 1
for i in range(n):
    row = []
    for j in range(n):
        row.append(count)
        count += 1
    m.append(row)
print(m)






