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