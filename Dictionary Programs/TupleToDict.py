#Convert a list of tuples into dictionary


#Using dict()
a = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
result = dict(a)
print(result)


#Using for loop
a = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
result = {}
for key, value in a:
    result[key] = value
print(result)
    


#Using map with dict
a = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
result = dict(map(lambda x: (x[0], x[1]), a))
print(result)