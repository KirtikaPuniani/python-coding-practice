#Counter to find the size of largest subset of anagram words.  --Counter to find size of largest subset of anagram
# Given an array of strings containing lowercase letters, the task is to find the size of the largest subset of words that are anagrams of each other. Two strings are said to be anagrams if they contain the same characters, 
# only in a different order.


#Using collections.Counter
from collections import Counter
def MaxAnagrams(input_string):
    words = input_string.split(" ")      #splits the input string into individual words.
    
    for i in range(len(words)):
        words[i] = ''.join(sorted(words[i]))      #sorts each word to group anagrams under a common form.
    
    frequencyDict = Counter(words)       #counts how many times each sorted word (anagram group) appears.
    print(max(frequencyDict.values()))    #finds the size of the largest anagram group.

if __name__ == "__main__":
    input_string = 'ant magenta magnate tan gnamate'
    MaxAnagrams(input_string)
    

#Using Dictionary Grouping
def largest_anagram_subset_size(words):
    anagram_dict = {}
    for word in words:
        sorted_word = ''.join(sorted(word))     #sorts each word to create a common key for its anagrams.
        if sorted_word not in anagram_dict:
            anagram_dict[sorted_word] = []
        anagram_dict[sorted_word].append(word)     #groups words that share the same sorted key.
    
    return max(len(val) for val in anagram_dict.values())    #finds the size of the largest anagram group.

words = ['ant', 'magenta', 'magnate', 'tan', 'gnamate']
print(largest_anagram_subset_size(words))

' '.join(sorted(word)): sorts each word to create a common key for its anagrams.
anagram_dict[sorted_word].append(word): groups words that share the same sorted key.
max(len(val) for val in anagram_dict.values()): finds the size of the largest anagram group.