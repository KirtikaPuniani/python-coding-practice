#Ways to sort list of dictionaries by values using lambda function


#Sort by single key
dict = [{'name': 'alice', 'age': 27},
        {'name': 'cherish', 'age': 21},
        {'name': 'neha', 'age': 31},
        {'name': 'tarun', 'age': 35}
]
print("Sorted by age:")
print(sorted(dict, key = lambda x: x['age']))        #sorts the list of dictionaries in asc order bases on age value of each dictioanry. If 2 items have the same age, python keeps them in the 
#same order as they appeared in the original list



#Sort by multiple keys
dict = [{'name': 'alice', 'age': 27},
        {'name': 'cherish', 'age': 21},
        {'name': 'neha', 'age': 31},
        {'name': 'tarun', 'age': 35}
]
print("\n Sorted by age and name:")
print(sorted(dict, key = lambda x: (x['age'], x['name'])))       #sorts the list of dictionaries in asc order bases on age value of each dictionary. If 2 items have the same age, python keeps 
#them in the same order as they appeared in the original list




#Sort by key in desc order
dict = [{'name': 'alice', 'age': 27},
        {'name': 'cherish', 'age': 21},
        {'name': 'neha', 'age': 31},
        {'name': 'tarun', 'age': 35}
]
print("\n Sorted by age (descending):")
print(sorted(dict, key = lambda x: x['age'], reverse=True))       #lambda function sorts the dictioanries based on the age value, reverse = True sorts in desc order