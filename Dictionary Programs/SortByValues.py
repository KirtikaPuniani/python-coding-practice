#Ways to sort list of dictionaries by values


#Sort by single key
from operator import itemgetter
dict = [{'name': 'alice', 'age': 27},
        {'name': 'cherish', 'age': 21},
        {'name': 'neha', 'age': 31},
        {'name': 'tarun', 'age': 35}
]
print("sorted by age: ", sorted(dict, key = itemgetter('age')))


#Sort by multiple keys
from operator import itemgetter
dict = [{'name': 'alice', 'age': 27},
        {'name': 'cherish', 'age': 21},
        {'name': 'neha', 'age': 31},
        {'name': 'tarun', 'age': 35}
]
print("sorted by age & name: ", sorted(dict, key = itemgetter('age', 'name')))