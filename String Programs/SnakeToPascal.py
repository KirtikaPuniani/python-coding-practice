#Convert Snake case to Pascal case
#Given a string in snake_case, the task is to convert in into PascalCase here each word dtarts with an upper case and there are no underscores.
#Eg: I/P: hello_everyone_iam_happy and O/P: HelloEveryoneIAmHappy



#Using split and capitalize
string = 'hello_everyone_iam_happy'
result = ''.join(word.capitalize() for word in string.split('_'))   
#split('_') splits the string into individual words at each underscore. Join() joins the list of words without any separator.
print(result)



#Using str.title() and replace()
string = 'hello_everyone_iam_happy'
result = string.replace("_", " ").title().replace(" ", "")     #replace("_", " ") handles the conversion of inderscores to spaces.
#title() ensures thaty the first letter of each word is capitalized. replace() removes any spaces ensuring the result is in pascal case.
print(result)



#using string.capwords()
import string
string = 'hello_everyone_iam_happy'
result = string.capwords(string.replace('_', '')).replace(' ', '')
print(result)



#using re.sub()
import re
string = 'hello_everyone_iam_happy'
result = re.sub(r"(^|_)([a-z])", lambda match: match.group(2).upper(), string)
#(^|_) matches either the start of the string (^) or an underscore (_)
#([a-z]) matches any lowercase letter (a-z) following the start of the string s or an underscore
#lambda match: match.group(2).upper() converts the matched lowercase letter (group 2) to uppercase
print(result)