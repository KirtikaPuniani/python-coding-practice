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


#Using Regular Expressions
import re
string = 'hello world'
string = re.sub("[aeiou]", "xx", string)     
#re.sub() removes all vowels. The pattern [aeiou] matches any vowel, and "" replaces them with nothing or anything specified within string.
print(string)



#Using list comprehension
string = 'hello world'
string = ''.join([c for c in string if c != 'l'])     #generates a list of characters in s but excludes "o". join() combines the list back into string
print(string)