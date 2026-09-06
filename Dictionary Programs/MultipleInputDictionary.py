#Dictionary with keys having multiple inputs
# In Python, dictionaries store data as key-value pairs. Tuples can be used as keys to represent multiple values, like coordinates or combinations, because they are immutable and hashable.
# Let's consider an example where tuples are used as keys to store multiple numbers together:
# points = {}
# points[(1, 2)] = "A"
# points[(3, 4)] = "B"
# print(points[(1, 2)]) 
# print(points[(3, 4)])
# Each key is a tuple representing multiple inputs.
# The value can be any data (here, "A" and "B").
# Access values using the tuple key.



#Dictioanry with multiple inputs as keys
dict = {}
dict[(1, 2)] = "Point A"          #Assigns the value "Point A" to the key (1, 2) in the dictionary.
dict[(3, 4)] = "Point B"          #Assigns the value "Point B" to the key (3, 4) in the dictionary.
dict[(5, 6)] = "Point C"          #Assigns the value "Point C" to the key (5, 6) in the dictionary.
print(dict[(1, 2)])          #Accesses and prints the value associated with the key (1, 2), which is "Point A".
print(dict[(3, 4)])          #Accesses and prints the value associated with the key (3, 4), which is "Point B".
print(dict[(5, 6)])         #Accesses and prints the value associated with the key (5, 6), which is "Point C".