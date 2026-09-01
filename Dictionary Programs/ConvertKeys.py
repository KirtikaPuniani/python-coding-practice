# Convert Key-Values List to Flat Dictionary

#Use dict()
a = [('name', 'Kirtika Puniani'), 
     ('age', 27), 
     ('profession', 'Python Developer'),
     ('status', 'unemployed')]
print(dict(a))


#Using dictionary comprehension
a = [('name', 'Kirtika Puniani'), 
     ('age', 27), 
     ('profession', 'Python Developer'),
     ('status', 'unemployed')]
print({key: value for key, value in a})



#Use for loop
a = [('name', 'Kirtika Puniani'), 
     ('age', 27), 
     ('profession', 'Python Developer'),
     ('status', 'unemployed')]
x = {}
for key, value in a:
    x[key] = value
print(x)



#Using zip
a = ['name', 'age', 'profession', 'status']
b = ['Kirtika Puniani', 27, 'Pyhton Developer', 'Unemployed']
x = dict(zip(a,b))
print(x)