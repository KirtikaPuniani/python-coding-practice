#Accept the strings which contains all vowels
#the task is toi check whether a given string contains all the vowels or not
#example: Input: 'education'
#Output: 'Accepted' (because it contains all vowels a, e, i, o, u)
#example: Input: 'hello'
#Output: 'Not Accepted' (because it does not contain all vowels)


#Using set operations
string = 'education'
vowels = set('aeiou')     #creates a set of vowels
if vowels.issubset(set(string.lower())):     #checks if all vowels are present
    print('Accepted')
else:
    print('Not Accepted')
    
    
#Using all() function
string = 'hello'
if all(vowel in string.lower() for vowel in 'aeiou'):     #checks if all vowels are present using all() function
    print('Accepted')
else:
    print('Not Accepted')