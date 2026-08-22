#String slicing to rotate a string
#Given a string of length n, rotate the string either, left (anticlockwise) by d positions or right(clockwise) by d positions where 0 <= d <= n.
#Input: "GeeksforGeeks", d=2
# Output: Left Rotation: "eksforGeeksGe" 
#         Right Rotation:  "ksGeeksforGee"


#Using string slicing
s = "HelloGoodMorningHowIsItGoing"
d = 2
left = s[d:] + s[:d]        #for left rotation take the substring from index d to end (s[d:]) and add the first d chars (s[:d])
right = s[-d:] + s[:-d]         #for right rotation take the substring from index d to end (s[-d:]) and add the first d chars (s[:-d])
print("left rotation:", left)
print("right rotation:", right)



#By extending the string
#this method doubles the string (s+s) so all possible rotations appear inside it. then the rotated version is obtained by slicing the extended string at the correct position.
s = "HelloGoodMorningHowIsItGoing"
d = 2
ext = s+s     #doubling the string contains all rotations
n = len(s)
left = ext[d: d+n]       #slice starting at d for n chars
right = ext[n-d: 2*n - d]       #slice starting d chars before n for n chars
print("Left Rotation:", left)
print("Right Rotation:", right)



#Rotation using collections.deque
from collections import deque
s = "HelloGoodMorningHowIsItGoing"
d = 2
dq = deque(s)       #converts the string into a deque so we can rotate efficiently

#left rotation
dq.rotate(-d)       #negative value rotates left; collect the left rotated string
left = ''.join(dq)

#right rotation
dq.rotate(d)    #reverses the previous rotation
dq.rotate(d)    #rotates right by d, collect the right rotated string
right = ''.join(dq)    #converts the deque back to a string

print("Left Rotation:", left)
print("Right Rotation", right)




#Using for loop
s = "HelloGoodMorningHowIsItGoing"
d = 2
n = len(s)

#Left Rotation
left = ""
for i in range(d, n):       #loops from index d --> end, adding all remaining chars
    left += s[i]
for i in range(d):         #appends the first d chars to complete the left rotation
    left += s[i]

#Right Rotation
right = ""
for i in range(n-d, n):     #adds the last d chars forst for right rotation
    right += s[i]
for i in range(n-d):       #appends the rest of the chars finishing teh right rotation
    right += s[i]

print("Left Rotation:", left)
print("Right Rotation:", right)