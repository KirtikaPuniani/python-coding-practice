#To check whether the string is symmetrical or palindrome

# A string is symmetrical if the first half of the string matches the second half (ignoring the middle character for odd length strings)
# A string is a palindrome if it reads the same forwards and backwards
# example: wowwow is both symmetrical and palindrome and abcba is palindrome but not symmetrical

#Using string slicing
string = "abcab"
half = len(string) //2
symmetrical = string[:half] == string[half:] if len(string) % 2 == 0 else string[:half] == string[half+1:]

palindrome = string == string[::-1]

print("Symmetrical" if symmetrical else "Not Symmetrical")
print("Palindrome" if palindrome else "Not Palindrome") 

# Explanation:
# string[:half] slices the first half of the string.
# string[half:] or string[half+1:] slices the second half depending on even/odd length.
# string[::-1] reverses the string for the palindrome check.
# Comparisons return True/False and determine the output.