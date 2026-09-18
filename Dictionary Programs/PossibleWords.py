#Possible words using given chars
#Given a list of owrds and a list of chars, print all valid words that can be formed using those chars. Repetetion of chars is not allowed.


#Using set and subsets
dict = ["go", "bat", "me", "eat", "goal", "boy", "run"]
ch = ['e', 'o', 'b', 'a', 'm', 'g', 'l']
x = set(ch)          #converts chars to a set for quick lookup
res = [w for w in dict if set(w).issubset(x)]       #set(w).issubset(x) check if all of the word exist in the given chars
print(res)



#Using dictionary county comparison
dict = ["go", "bat", "me", "eat", "goal", "boy", "run"]
ch = ['e', 'o', 'b', 'a', 'm', 'g', 'l']
for word in dict:
    valid = True
    for a in word:      #iterates each char in the word
        if a not in ch or word.count(a) > ch.count(a):        #ensures the letter exists and isn't  used more times than available
            valid = False
            break
    if valid:
        print(word)        #prints word that can be formed using given chars
        

#Using list filtering
dict = ["go", "bat", "me", "eat", "goal", "boy", "run"]
ch = ['e', 'o', 'b', 'a', 'm', 'g', 'l']
for i in dict:       #checks each in list
    if all(i.count(c) <= ch.count(c) for c in set(i)):     #ensures every character in the word exists within the available characters and isn’t overused.
        print(i)
        

#Recursive combination approach