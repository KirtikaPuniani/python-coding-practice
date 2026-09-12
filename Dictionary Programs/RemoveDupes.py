#Remove all duplicate words from a given sentence


#Using dict.fromkeys
string = '''my name is kirtika puniani. my brother's name is cherish'''
str = string.split()
string_op = list(dict.fromkeys(str))
result = ' '.join(string_op)
print(result)