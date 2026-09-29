#Remove tuples of length k


#Using list comprehension
x = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
k = 1
output = [ele for ele in x if len(ele) != k]        #[ele for ele in x if len(ele) != k] creates a new list containing only the tuples whose length is not equal to k
print(str(output))



#Using filter + lambda + len
x = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
k = 1
output = list(filter(lambda x: len(x) != k, x))       #applies a filter function that keeps only the tuples whose length is not equal to k
print(str(output))



#Using a loop
x = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
k = 1
output = []
for t in x:          #Iterates through each tuple and appends it to res only if its length is not equal to k
    if len(t) != k:
        output.append(t)
print(output)



#Using map and lambda function
x = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
k = 1
output = list(map(lambda x: x, filter(lambda x: len(x) != k, x)))
#list(map(lambda x: x, filter(lambda x: len(x) != k, x))): filters t1 to keep only tuples whose length is not k and returns them as a list
print(output)