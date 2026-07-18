#Given a string and the task is to check whether it is a palindrome. A palindrome is a string that reads same foreward and backward.
#Example : "racecar" is a palindrome, "hello" is not a palindrome.


string = "racecar"
def is_palindrome(s):
    if s == s[::-1]:      #Used slicing
        return True
    else:
        return False
print(is_palindrome(string))




#using user input string
def is_palindrome(s):
    return s == s[::-1]
string = input("Enter a string to check if it is a palindrome: ")
if is_palindrome(string):
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")
    
    
#Using two pointer 
string = 'wow'
a, b = 0, len(string) - 1
is_palindrome = True
while a < b:
    if string[a] != string[b]:
        is_palindrome = False
        break
    a += 1
    b -+ 1

if is_palindrome:
    print("Yes")
else:
    print("No")
#Explanation:
#While loop compares characters from both ends towards the center as long as a < b. If no match is found, the pointers move inward for the next
#comparison. After the loop, it prints yes or no accordingly if the string is palindrome or not.




#Using all with generator expression
string = "xyxyxyxh"
if all(string[i] == string[-i-1] for i in range(len(string) //2)):
    #range(len(string)//2) generates indices for the first half of the string and s[-i-1] accessed characters from the end of the string
    #string[i] == string[-i-1] checks quality for mirrored positions and all() returns true only if evry comparison is true
    print("Yes")
else:
    print("No")
    
    
    
#Using reversed and join
string = 'Geeks'
reverse = ''.join(reversed(string))
if string == reversed:
    print("Yes")
else:
    print("No")