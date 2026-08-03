#remove all duplicates from a string

#Using dict.fromkeys
string = 'hello everyone good morning'
result = ' '.join(dict.fromkeys(string))
print(result)