#Given a string print only the words whose lengths are even
#Example: Input: 'hello everyone good morning'
#Output: 'hello good'


#Using list comprehension
string = 'hello everyone good morning'
words = string.split()     #splits the string into a list of words
even_words = [w for w in words if len(w) % 2 == 0]     #filters words with even length
result = ' '.join(even_words)      #combines the filtered words back into a string
print(result)




#Using filter with lambda function
string = 'hello everyone good morning'
words = string.split()     #splits the string into a list of words
even_words = list(filter(lambda w: len(w) % 2 == 0, words))     #filters words with even length using filter and lambda
result = ' '.join(even_words)      #combines the filtered words back into a string
print(result)




#Using Generator expression
string = 'hello everyone good morning'
words = string.split()     #splits the string into a list of words
even_words = (w for w in words if len(w) % 2 == 0)     #creates a generator for words with even length
result = ' '.join(even_words)      #combines the filtered words back into a string
print(result)