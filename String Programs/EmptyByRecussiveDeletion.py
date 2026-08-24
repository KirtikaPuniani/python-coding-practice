#Check if a string can become empty by recursive deletion using slicing
#Given a string S and a substring 'sub' the task is to determine whether 'S' can be reduced to an empty string by repeatedly deleting one occurence at a time of the substring 'sub' whenever 
# it appears in the string
#Example:
# Input:
# s = "aaaaaa"
# sub = "aa"

# Output:
# True (string becomes empty)

# Explanation:
# "aaaaaa" → remove "aa" → "aaaa"  
# "aaaa"   → remove "aa" → "aa"  
# "aa"     → remove "aa" → ""  



#While loop with slicing
s = 'IamKirtikaIamHappyIamContentIamEnoughIamSupportive'
sub = 'Iam'
while True:
    ind = s.find(sub)     #searches for the substring sub inside s and returns it starting order
    if ind == -1:       #the substring is not found anymore so the loop stops
        break
    s = s[:ind] + s[ind + len(sub):]             #removes the found substring by keeping the part before it and after it
result = (s == "")            #Checks whether the final strig is empty
print(result)




#Recursive deletion using slicing
#recursive deletion using slicing means removing a substring from a string again and again by cutting it out using slicing (s[:]). The process keeps calling itself until either the string 
# becomes empty or no more deletions are possible
def recursiveDeletion(s, sub):
    if not s:        #if the string is empty, return True
        return True
    ind = s.find(sub)        #find the first occurence of the substring
    
    if ind != -1:
        s1 = s[:ind] + s[ind + len(sub):]         #if found - remove it using slicing: s[:ind] + s[ind + len(sub):]
        return recursiveDeletion(s1, sub)       #call function again with the updates string
    return False           #if not found- return false because the string can't be reduced further
s = 'IamKirtikaIamHappyIamContentIamEnoughIamSupportive'
sub = 'Iam'

result = recursiveDeletion(s, sub)
print(result)




#Using replace() recursively
#this method removes the substring using replace() inside a recursive function. each recursive call removes the substring again and again until either the string becomes empty or no more 
# removals are possible
def replaceRecursive(s, sub):           #defines a recursive function that keeps removing the substring
    if not s:           #if the string becomes rmpty, return True   
        return True
    s1 = s.replace(sub, "")        #removes all occurences of sub from s and stores the updated string in s1
    
    if s1 == s:      #checks if nothing was removes
        return False      #if true: substring no longer exists return False
    return replaceRecursive(s1, sub)
s = 'IamKirtikaIamHappyIamContentIamEnoughIamSupportive'
sub = 'Iam'
result = replaceRecursive(s, sub)
print(result)




#Iterative replace() loop
#an iterative replace() loop repeatedly calls replace() inside a loop to update a string step by step until all desired changes are applied
s = 'IamKirtikaIamHappyIamContentIamEnoughIamSupportive'
sub = 'Iam'
previous = None
while s != previous:
    previous = s
    s = s.replace(sub, "")
print(s == " ")