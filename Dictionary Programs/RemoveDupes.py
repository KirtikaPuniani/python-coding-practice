#Remove all duplicate words from a given sentence


#Using dict.fromkeys
string = '''my name is kirtika puniani. my brother's name is cherish'''
str = string.split()       #string.split splits the sentence into words
string_op = list(dict.fromkeys(str))       #dict.fromkeys creates keys from words, automatically removing duplicates while maintaining their first occurence. list function converts dictionary keys back to a list
result = ' '.join(string_op)     #join function joins list elements back into a string separated by spaces
print(result)



#Using list comprehension with set
string = '''my name is kirtika puniani. my brother's name is cherish'''
str = string.split()
seen = set()
string_op = [word for word in str if not (word in seen or seen.add(word))]
result = ' '. join(string_op)
print(result) 