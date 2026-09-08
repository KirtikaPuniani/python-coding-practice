#K-th Non repeating character in a string


#Using collections.Counter
from collections import Counter
string = 'happybithdaytoyouhappyhappybithdaytoyou'
k = 3
count = Counter(string)          #Counts the occurrences of each character in the string.
result = [ch for ch in string if count[ch] == 1]          #Creates a list of characters that occur only once in the string, preserving their order of first occurrence.
print(result[k-1] if len(result) >= k else None)          #Prints the k-th non-repeating character if it exists; otherwise prints None.