#Dictionary to find mirror character in a string
# Given a string and a number N, we need to mirror the characters from the N-th position to the end of the string in alphabetical order. In a mirror operation:
# 'a' becomes 'z'
# 'b' becomes 'y'
# 'c' becomes 'x', and so on.
#I/P: n = 3, word = paradox
#O/P: paizwlc
# Explanation: We mirror characters from position 3 to end.

# We can solve this problem in Python using the Dictionary data structure. Below are the steps:

# The mirror value of 'a' is 'z', 'b' is 'y', etc.
# Create a dictionary mapping each character to its mirror value.
# Traverse characters from position N to the end of the string and replace them using the dictionary.
# Concatenate the unchanged prefix (first N-1 characters) with the mirrored part.




def mirrorChars(input, k):
    original = 'abcdefghijklmnopqrstuvwxyz'
    reverse = 'zyxwvutsrqponmlkjihgfedcba'
    dictChars = dict(zip(original, reverse))
    
    prefix = input[0:k-1]
    suffix = input[k-1:]
    mirror = ''
    
    for i in range(0, len(suffix)):
        mirror = mirror + dictChars[suffix[i]]
    print(prefix + mirror)
    
if __name__ == '__main__':
    input = 'paradox'
    k = 3
    mirrorChars(input, k)