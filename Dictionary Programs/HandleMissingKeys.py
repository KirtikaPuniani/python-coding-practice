#Handling missing keys in dictionaries

#Using defaultdict
from collections import defaultdict
dict = defaultdict(lambda: 'Key not found')          #Creates a defaultdict with a default value for missing keys that returns defualt value for missing keys instead of raising a KeyError.
dict['name'] = 'Alice'
dict['age'] = 27
print(dict['name'])          #Accesses an existing key, returns its value.
print(dict['profession'])          #Accesses a missing key, returns the default value 'Key not found'.



#Using get method
dict = {'name': 'Alice', 'age': 27, 'profession': 'Python Developer', 'status': 'unemployed'}
print(dict.get('name'))          #Accesses an existing key, returns its value.
print(dict.get('profession'))          #Accesses a missing key, returns None (default) or a specified default value.
print(dict.get('salary', 'Key not found'))          #Accesses a missing key, returns the specified default value 'Key not found'.



