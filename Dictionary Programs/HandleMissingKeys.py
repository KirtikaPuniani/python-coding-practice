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



#Using setdefault method
dict = {'name': 'Alice', 'age': 27, 'profession': 'Python Developer', 'status': 'unemployed'}
print(dict.setdefault('name'))          #Accesses an existing key, returns its value.
print(dict.setdefault('profession'))          #Accesses a missing key, returns None (default) or a specified default value.
print(dict.setdefault('salary', 'Key not found'))          #Accesses a missing key, returns the specified default value 'Key not found' and adds the key-value pair to the dictionary.
print(dict['name'])      #Accesses the existing key 'name', returns its value.
print(dict['salary'])      #Accesses the newly added key 'salary', returns its value 'Key not found'.    #Prints the updated dictionary with the new key-value pair added for the missing key 'salary'.