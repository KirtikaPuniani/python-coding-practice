#Remove letters from a string


#Using replace
string = "hello world"
string = string.replace("l", "")     #replaces every "l" with an empty string "" or anything specified after the letter that needs to be replaced
print(string)      #and replacement creates a new string and the original string remains unchanged


#Using filter function
#filter function provides an efficient way to filter out characters baces on a condition. It returns an iterator which can be converted back to a string
string = "hello world"
string = "".join(filter(lambda c: c != "o", string))  #filter checks evry charac ter in string and removes 'o' and join merges the remaining char into single string
print(string)
