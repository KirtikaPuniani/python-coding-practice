#Print Anagrams together using list and dictionary
#Anagrams are words formed by rearranging the letters of another word, using all original letters exactly once
# def print_anagrams(words):
#     anagram_dict = {}
#     for word in words:
#         # Create a key by sorting the characters of the word
#         key = ''.join(sorted(word))
#         # Add the word to the list of its anagram group
#         if key in anagram_dict:
#             anagram_dict[key].append(word)
#         else:
#             anagram_dict[key] = [word]
    
#     # Print all anagram groups
#     for group in anagram_dict.values():
#         if len(group) > 1:  # Only print groups with more than one word
#             print(' '.join(group))

# # Example usage
# words = ["listen", "silent", "enlist", "hello", "world"]
# print_anagrams(words)

#Using Counter from collections
from collections import Counter, defaultdict
words = ["listen", "silent", "enlist", "hello", "world"]
result = defaultdict(list)
for word in words:
    # Create a key by counting the characters of the word
    key = tuple(sorted(Counter(word).items()))
    result[key].append(word)
print(list(result.values()))  # Print all anagram groups