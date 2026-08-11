#Find words which are greater than given length k
#A string is given and you have to find all the words which are greater than given length k. You have to print the words which are greater than given length k.

#I/P: string = "Hello World Python Programming"
#     k = 4
#O/P: Words greater than length 4: ['Hello', 'World', 'Python', 'Programming']
#Explanation: The Output is the list of words which are greater than given length k.


def find_words(string, k):
    words = string.split()
    result = []
    for word in words:
        if len(word) > k:
            result.append(word)
    return result

#Driver Code
if __name__ == '__main__':
    string = 'Hello World Python Programming'
    k = 7
    words = find_words(string, k)
    print(f"Words greater than length {k}: {words}")
    
#Time Complexity: O(n), where n is the number of words in the string.
#Space Complexity: O(n), where n is the number of words in the string.




#Using list comprehension
string = 'Hello World Python Programming'
k = 10
print([word for word in string.split() if len(word) > k])



#Using lambda function
string = 'Hello i am Kirtika Puniani'
k = 5
a = string.split()
b = list(filter(lambda x: (len(x) > k), a))
print(b)