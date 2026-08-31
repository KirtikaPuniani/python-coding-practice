#Ways to sort list of dictionaries by values using lambda function


#Sort by single key
dict = [{'name': 'alice', 'age': 27},
        {'name': 'cherish', 'age': 21},
        {'name': 'neha', 'age': 31},
        {'name': 'tarun', 'age': 35}
]
print("Sorted by age:")
print(sorted(dict, key = lambda x: x['age']))



#Sort by multiple keys
dict = [{'name': 'alice', 'age': 27},
        {'name': 'cherish', 'age': 21},
        {'name': 'neha', 'age': 31},
        {'name': 'tarun', 'age': 35}
]
print("\n Sorted by age and name:")
print(sorted(dict, key = lambda x: (x['age'], x['name'])))