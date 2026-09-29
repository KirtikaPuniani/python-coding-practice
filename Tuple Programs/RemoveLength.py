#Remove tuples of length k


#Using list comprehension
x = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
k = 1
output = [ele for ele in x if len(ele) != k]
print(str(output))