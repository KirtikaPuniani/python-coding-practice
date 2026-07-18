#Given a matrix conatining string, the task is to perform vertical concatenation, where elements from each column are joined together to form a
#single string for that column.


# Vertical Concatenation of Matrices

#Using pandas Dataframe and apply
import pandas as pd
matrix = [['I', 'am', 'a', 'intelligent', 'person'], ['and', 'I', 'can', 'do', 'anything'], ['I', 'put', 'my', 'mind', 'to']]
df = pd.DataFrame(matrix)
result = df.fillna('').apply(''.join)
print(result)

# Explanation:
# pd.DataFrame(t1): Converts the matrix into a structured DataFrame.
# fillna(''): Replaces missing values in shorter rows with empty strings.
# apply(''.join): Joins strings in each column efficiently.
# list(res): Converts the resulting concatenated column data back into a list.






#Using numpy transpose and ravel
import numpy as np
matrix = [['I', 'am', 'a', 'intelligent', 'person'], ['and', 'I', 'can', 'do', 'anything'], ['I', 'put', 'my', 'mind', 'to']]
m = max(len(x) for x in matrix)  # Find the maximum row length
p = [x + [''] * (m - len(x)) for x in matrix] # Pad shorter rows with empty strings
array = np.array(p).T
result = [''.join(row) for row in array]
print(str(result))

# Explanation:
# max(len(x) for x in lst): finds the maximum sublist length (2).
# [x + [''] * (m - len(x)) for x in lst]: pads shorter lists with ' ' [['Gfg','good'], ['is','for'], ['Best','']].
# np.array(p).T: converts to NumPy array and transposes: [['Gfg','is','Best'], ['good','for','']].
# [''.join(row) for r in arr]: joins each transposed row: ['GfgisBest','goodfor'].





#Using join + list comprehension + zip_longest
from itertools import zip_longest
matrix = [['I', 'am', 'a', 'intelligent', 'person'], ['and', 'I', 'can', 'do', 'anything'], ['I', 'put', 'my', 'mind', 'to']]
result = ["".join(col) for col in zip_longest(*matrix, fillvalue='')]
print(str(result))

# Explanation:
# zip_longest(*t1, fillvalue=""): transposes the matrix and fills missing elements with "".
# join(col): concatenates strings column-wise.
# list comprehension builds the final result.