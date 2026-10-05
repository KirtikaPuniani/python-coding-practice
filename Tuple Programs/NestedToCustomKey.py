#Convert nested tuple to custom key dictionary
#Given a nested tuple, the task is to convert each inner tuple into a dictionary with predefined custom keys. Each tuple represents a structured record, and the goal is to map every element of the tuple to the appropriate key.
#For example,
#Input: ((4, 'Gfg', 10), (3, 'is', 8), (6, 'Best', 10))
#Output: [{'key': 4, 'value': 'Gfg', 'id': 10}, {'key': 3, 'value': 'is', 'id': 8}, {'key': 6, 'value': 'Best', 'id': 10}].



#Using dict with zip
x = ((4, 'Gfg', 10), (3, 'is', 8), (6, 'Best', 10))
keys = ['key', 'value', 'id']
output = [dict(zip(keys, sub)) for sub in x]
#zip(keys, sub) pairs each key with the corresponding element from the tuple. Example: zip(['key','value','id'], (4, 'Gfg', 10)) --> [('key', 4), ('value', 'Gfg'), ('id', 10)]
#dict() converts the paired values into a dictionary.
#[dict(zip(keys, sub)) for sub in a] applies this logic to every tuple in a and stores results in a list.
print(output)