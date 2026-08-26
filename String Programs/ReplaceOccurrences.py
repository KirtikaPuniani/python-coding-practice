#Replace all occurrences of a substring in a string
#example: I/P - "python java python html python"
#Replace "python" --> "c++"
#Output: "c++ java c++ html c++"


#Using replace()
string = "python java python html python"
result = string.replace('python', 'c++')
print(result)



#Using re.sub()
import re
string = "python java python html python"
result = re.sub("python", "c++", string)
print(result)



#Using string splitting and joining
string = 'python java python html python'
result = 'c++'.join(string.split('python'))
print(result)


#Using a manual loop
string = 'python java python html python'
target = 'python'
replacement = 'c++'
result = ""

i = 0
while i < len(string):
    if string[i:i+len(target)] == target:     #take a slice of the string from index i to i+len(target) and check if it matches the target substring
        result += replacement        #if a match is found, append the replacement string to result
        i += len(target)           #move the index forward by the length of the target substring to skip the replaced part
    else:
        result += string[i]      #append the current char to result
        i += 1        #move the index forward by 1 to continue checking the next char
print(result)