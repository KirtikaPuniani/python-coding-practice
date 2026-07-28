#check if the string contains substring

#given two strings check whether a substring is in the given string
#example: string1 = 'iamhappytoday', string2 = 'am', O/P = yes
#example: string1 = 'iamhappytoday', string2 = 'for', O/P = no


#using in
#the in operator inpython checks if one string occurs within another. It evaluates to True if string is present in the main string otherwise False.
string = 'I am not able to understand my emotions and work together today'
if "for" in string:
    print("Substring found")
else:
    print("Substring not found")
    
if "able" in string:
    print("Substring found")
else:
    print("Substring not found")