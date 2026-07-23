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