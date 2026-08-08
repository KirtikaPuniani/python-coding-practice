#Check if a string contains any special character. If any special character is found, don't accept the string.


#Using regular expression
import re
def run(string):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')      #regex pattern to find special characters
    if(regex.search(string) == None):      #searches the string for special characters
        print("String accepted")
    else:
        print("String rejected")
#Driver Code
if __name__ == '__main__':
    string = 'Hello World'
    string2 = 'He@ll$o W!or/ld'
    run(string)     #calling run fuction
    run(string2)    #calling run function
    
    
    
#OR#
string = 'Hello World'
string.split()
count = 0
regex = '[@_!#$%^&*()<>?/\|}{~:]'      #regex pattern to find special characters
for i in range(len(string)):
    if string[i] in regex:      #searches the string for special characters
        count += 1
if count:
    print("String rejected")
else:
    print("String accepted")
    
    
    
    
#Using inbuilt function
def has_special_char(string):
    for c in string:
        if not (c.isalpha() or c.isdigit() or c == ' '):
            return True
    return False
string = 'He@ll$o W!or/ld'
if has_special_char(string):
    print("String rejected")
else:
    print("String accepted")

string = 'Hello World'
if has_special_char(string):
    print("String rejected")
else:
    print("String accepted")