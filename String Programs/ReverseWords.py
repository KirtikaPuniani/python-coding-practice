#Given the string the task is to reverse the words in it without changing the words itself
#example: string - 'Learning python is easy'
#then when reversed the strng should be - 'easy is python learning'

#using split() and join()
string = "Learning python is easy"
result = ' '.join(string.split()[::-1])
print(result)
#explanation: 
#string.split() splits the string into the list of words
#[::-1] reverses the list of words
#''.join() concatinates the reversed words into a single string separated by spaces



#Using loops
string = "Learning python is easy"
words = string.split()
result = ""

for word in reversed(words):
    result += word + " "

result = result.strip()
print(result)
# Explanation:
# s.split() splits the string into a list of words
# reversed(words) creates an iterator to traverse the list in reverse order.
# Inside the loop, res += word + " " appends each word followed by a space.
# res.strip() removes the trailing space at the end.




#Using deque from collections
from collections import deque
string = "Learning python is easy"
words = deque(string.split())
result = ""
while words:
    result += words.pop() + " "
result = result.strip()
print(result)
# Explanation:
# deque(s.split()) creates a deque for fast popping from both ends.
# words.pop() removes and returns the last word from the deque.
# res += ... appends the word followed by a space.
# res.strip() removes trailing space.





#Using Stack
string = "Learning python is easy"
words = string.split()
stack = []
for word in words:
    stack.append(word)
result = ""
while stack:
    result += stack.pop() + " "
result = result.strip()
print(result)
# Explanation:
# stack.append(word) pushes each word onto the stack.
# stack.pop() removes the last word pushed, giving reversed order.