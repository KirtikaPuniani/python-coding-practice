#Replace multiple words with k
#replace all occurences of specific words in a string a single replcaement word k.
#eg: text = 'apple banana oranges'     words_to_replace = ['apple', 'banana']
#    O/P = 'k k oranges'


#Using list comprehension
s = 'apple banana oranges'
words_to_replace = ['apple', 'banana']
k = 'kiwi'
result = ' '.join([k if word in words_to_replace else word for word in s.split()])        #checks each word; if it's in words_to_replace, it replaces it with k
print(result)



#Using re.sub() with regex
import re
s = 'apple banana oranges'
words_to_replace = ['apple', 'oranges']
k = 'strawberry'
result = re.sub("|".join(sorted(words_to_replace, key = len, reverse = True)), k, s)
print(result)