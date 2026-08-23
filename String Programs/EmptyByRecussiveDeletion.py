#Check if a string can become empty by recursive deletion using slicing
#Given a string S and a substring 'sub' the task is to determine whether 'S' can be reduced to an empty string by repeatedly deleting one occurence at a time
#of the substring 'sub' whenever it appears in the string
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
    ind = s.find(sub)
    if ind == -1:
        break
    s = s[:ind] + s[ind + len(sub):]
result = (s == "")
print(result)