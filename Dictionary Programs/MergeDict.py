#Merging or concatenating 2 dictionaries


#Using | Operator
dict1 = {'x' : 123, 'y' : 456}
dict2 = {'a' : 789, 'b' : 345}
x = dict1 | dict2         #| operator combines two dictionaries into a new dictionary. Duplicate keys are handeled by keeping the value from the dictionary on the right
print(x)



#Using dictionary unpacking
dict1 = {'x' : 123, 'y' : 456}
dict2 = {'a' : 789, 'b' : 345}
x = {**dict1, **dict2}      #**dict1, **dict2 unpack the key value pairs of dictionaries into the new dictionary. In case of duplicates keys from dictionary 2 overwrites duplicates from dictionary 1
print(x)



#Using update
dict1 = {'x' : 123, 'y' : 456}
dict2 = {'a' : 789, 'b' : 345}
dict1.update(dict2)        #adds all key value pairs from dict2 to dict1. If a key exists in both dict1 and dict2 the value from dict2 replaces the value in dict1
print(dict1)



#Use loop
dict1 = {'x' : 123, 'y' : 456}
dict2 = {'a' : 789, 'b' : 345}
x = dict1.copy()       #creates a shallow copy of dict1 to preseve the original dictionary.
for key, value in dict2.items():      #for loop iterates through each key value pair in dict2 and adds or updates in x
    x[key] = value
print(x)