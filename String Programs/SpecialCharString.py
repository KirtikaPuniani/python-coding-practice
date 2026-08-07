#Check if that string contains any special character. If any special character is found, don't accept the string.


#Using regular expression
import re
def run(string):
    regex = re.compiple('[@_!#$%^&*()<>?/\|}{~:]')      #regex pattern to find special characters
    if(regex.search(string) == None):      #searches the string for special characters
        print("String accepted")
    else:
        print("String rejected")
#Driver Code
if __name__ == '__main__':
    string = 'Hello World'
    run(string)     #calling run fuction