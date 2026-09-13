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
seen = set()       #set(), empty set created to record words already seen
string_op = [word for word in str if not (word in seen or seen.add(word))]     #The condition not(word in seen or seen.add(word)) adds a word to result only if it hasn't appeared before
result = ' '. join(string_op)       #join function joins words back to form the final sentence
print(result) 


#Using set with join
string = '''my name is kirtika puniani. my brother's name is cherish'''
str = string.split()       #split function splits the sentence into words. 
string_op = list(set(str))       #set function removes duplicates automatically since sets can;t contain repeated elements. Converting set back to a list may change the order of the words
result = ' '.join(string_op)
print(result)


#Using simple loop
string = '''my name is kirtika puniani. my brother's name is cherish'''
str = string.split()
result = []
for word in str:       #the loop checks each word in str. If word not already in result, it's added to maintain forst occurence
    if word not in result:
        result.append(word)
string_op = ' '.join(result)        #join function rebuilds the sentence from unique words
print(string_op)