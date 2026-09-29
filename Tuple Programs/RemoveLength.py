#Remove tuples of length k


#Using list comprehension
x = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
k = 1
output = [ele for ele in x if len(ele) != k]        #[ele for ele in x if len(ele) != k] creates a new list containing only the tuples whose length is not equal to k
print(str(output))



#Using filter + lambda + len
x = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
k = 1
output = list(filter(lambda x: len(x) != k, x))
print(str(output))