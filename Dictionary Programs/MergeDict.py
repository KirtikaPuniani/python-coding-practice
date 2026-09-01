#Merging or concatenating 2 dictionaries


#Using | Operator
dict1 = {'x' : 123, 'y' : 456}
dict2 = {'a' : 789, 'b' : 345}
x = dict1 | dict2         #| operator combines two dictionaries into a new dictionary. Duplicate keys are handeled by keeping the value from the dictionary on the right
print(x)