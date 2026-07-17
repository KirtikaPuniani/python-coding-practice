#Given a matrix conatining string, the task is to perform vertical concatenation, where elements from each column are joined together to form a
#single string for that column.




#Using pandas Dataframe and apply
import pandas as pd
matrix1 = [['I', 'am', 'a', 'intelligent', 'person'], ['and', 'I', 'can', 'do', 'anything'], ['I', 'put', 'my', 'mind', 'to']]
df = pd.DataFrame(matrix1)
result = df.fillna('').apply(''.join)
print(result)

# Explanation:
# pd.DataFrame(t1): Converts the matrix into a structured DataFrame.
# fillna(''): Replaces missing values in shorter rows with empty strings.
# apply(''.join): Joins strings in each column efficiently.
# list(res): Converts the resulting concatenated column data back into a list.