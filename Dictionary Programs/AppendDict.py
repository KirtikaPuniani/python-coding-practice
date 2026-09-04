#Append Dictionary Keys and Values in order in dictionary


#Using zip and dictionary constructor
keys = ['name', 'age', 'profession', 'status']
values = ['Alice', 30, 'Engineer', 'Unemployed']
dict1 = dict(zip(keys, values))
print(dict1)