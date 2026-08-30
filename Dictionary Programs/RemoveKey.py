#Ways to remove a key from dictionary


#Using pop()
dict ={'name': 'Daphne Barnes',
       'age': 27,
       'occupation': 'Developer',
       'city': 'Rohtak'}
result = dict.pop('city')
print(dict)
print(result)



#Using del()
dict ={'name': 'Daphne Barnes',
       'age': 27,
       'occupation': 'Developer',
       'city': 'Rohtak'}
del dict['city']
print(dict)



#Using pop() with default value
dict ={'name': 'Daphne Barnes',
       'age': 27,
       'occupation': 'Developer',
       'city': 'Rohtak'}
result = dict.pop('country', 'key not found')
print(dict)
print(result)



#Using popitem() for last key removal
dict ={'name': 'Daphne Barnes',
       'age': 27,
       'occupation': 'Developer',
       'city': 'Rohtak'}
x = dict.pop()
print(dict)
print(x)