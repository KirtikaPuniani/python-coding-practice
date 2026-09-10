#Counter to find the size of largest subset of anagram words.  --Counter to find size of largest subset of anagram
# Given an array of strings containing lowercase letters, the task is to find the size of the largest subset of words that are anagrams of each other. Two strings are said to be anagrams if they contain the same characters, 
# only in a different order.


#Using collections.Counter
from collections import Counter
def MaxAnagrams(input_string):
    words = input_string.split(" ")
    
    for i in range(len(words)):
        words[i] = ''.join(sorted(words[i]))
    
    frequencyDict = Counter(words)
    print(max(frequencyDict.values()))

if __name__ == "__main__":
    input_string = 'ant magenta magnate tan gnamate'
    MaxAnagrams(input_string)