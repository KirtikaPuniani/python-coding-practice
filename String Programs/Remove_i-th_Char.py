#Removing i-th character from a string
#Given a string and an index i, remove the character at the i-th position and return the resulting string.
#Eg: I/P: 'PythonProgramming' and i = 6
#O/P: 'Pythonrogramming'


#Using string slicing
string = 'PythonProgramming'
i = 6
op = string[:i] + string[i+1:]    #s[:i] extracts chars from the start up to index i(but not excluding) and s[i+1:] extracts chars from index i+1 to the end
print(op)



#Using join() with list comprehension
string = 'KirtikaPuniani'
i = 6
res = ''.join([string[j] for j in range(len(string)) if j != i])      #for loop iterates through all indices and skips the i-th char and join converts the list of chars back into the string
print(res)



#Using replace() with slicing
string = 'PestoPastaWithParmesan'
i = 9
result = string[:i] + string[i:].replace(string[i], '', 1)     #removes i-th char by joining the part before i with the remaining substring after deleting s[i]
print(result)


#Using a for loop
string = 'IAmIronMan'
i = 1
result = ''
for x in range(len(string)):      #for loop iterates through all indices skipping the i-th char
    if x != i:
        result += string[x]      #concatenates chars to res one by one
print(result)