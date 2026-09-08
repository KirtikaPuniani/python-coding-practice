#K-th Non repeating character in a string


#Using collections.Counter
from collections import Counter
string = 'happybithdaytoyouhappyhappybithdaytoyou'
k = 3
count = Counter(string)          #Counts the occurrences of each character in the string.
result = [ch for ch in string if count[ch] == 1]          #Creates a list of characters that occur only once in the string, preserving their order of first occurrence.
print(result[k-1] if len(result) >= k else None)          #Prints the k-th non-repeating character if it exists; otherwise prints None.
# Counter(s): creates a dictionary of individual characters as keys and their frequencies as values ({'e': 4, 'g': 2, 'k': 2, 's': 2, 'f': 1, 'o': 1, 'r': 1}).
# [ch for ch in s if c[ch] == 1]: collects characters that appear only once 'c'.
# res[k - 1] if k <= len(res) else None: prints the k'th element of "res" if k is less than the length of "res", else it prints none.


#Using OrderedDict
from collections import OrderedDict
string = 'happybithdaytoyouhappyhappybithdaytoyou'
k = 9
frequency = OrderedDict()          #Creates an ordered dictionary to maintain the order of first occurrence of characters.
for ch in string:
    frequency[ch] = frequency.get(ch, 0) + 1          #Updates the frequency count of each character in the ordered dictionary.
non_repeating = [ch for ch, count in frequency.items() if count == 1]          #Creates a list of characters that occur only once in the ordered dictionary, preserving their order of first occurrence.
print(non_repeating[k-1] if len(non_repeating) >= k else None)          #Prints the k-th non-repeating character if it exists; otherwise prints None.



#