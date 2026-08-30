#Program to find the sum of all items in a dictionary


#Using sum
dict = {'a': 100, 'b': 300, 'c': 500}
result = sum(dict.values())
print(result)



#Using list comprehension and sum
dict = {'a': 100, 'b': 300, 'c': 500}
result = sum([dict[key] for key in dict])
print(result)



#Using a for loop
dict = {'a': 100, 'b': 300, 'c': 500}
result = 0
for value in dict.values():
    result += value
print(result)



#Using map with a lambda
dict = {'a': 100, 'b': 300, 'c': 500}
result = sum(map(lambda key: dict[key], dict))
print(result)