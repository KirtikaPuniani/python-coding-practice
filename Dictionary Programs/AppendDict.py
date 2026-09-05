#Append Dictionary Keys and Values in order in dictionary


#Using zip and dictionary constructor
keys = ['name', 'age', 'profession', 'status']
values = ['Alice', 30, 'Engineer', 'Unemployed']
dict1 = dict(zip(keys, values))       #zip(keys, values) - Pairs keys with their corresponding values and dict() creates the dictionary in insertion order
print(dict1)



#Using for loop with Direct Assignment
keys = ['name', 'age', 'profession', 'status']
values = ['Alice', 30, 'Engineer', 'Unemployed']
dict = {}
for k, v in zip(keys, values):       #zip(keys, value) combimes keys and values for iteration
    dict[k] = v           #Directly assigns each key-value pair to the dictionary in the order they are zipped together. Each key-value pair is appended to the dictionary using assignment, preserving the order of insertion.
print(dict)