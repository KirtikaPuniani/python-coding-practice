#Removing i-th character from a string
#Given a string and an index i, remove the character at the i-th position and return the resulting string.
#Eg: I/P: 'PythonProgramming' and i = 6
#O/P: 'Pythonrogramming'


#Using string slicing
string = 'PythonProgramming'
i = 6
op = string[:i] + string[i+1:]
print(op)