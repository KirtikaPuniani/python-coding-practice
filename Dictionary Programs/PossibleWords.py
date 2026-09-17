#Possible words using given chars
#Given a list of owrds and a list of chars, print all valid words that can be formed using those chars. Repetetion of chars is not allowed.


#Using set and subsets
dict = ["go", "bat", "me", "eat", "goal", "boy", "run"]
ch = ['e', 'o', 'b', 'a', 'm', 'g', 'l']
x = set(ch)
res = [w for w in dict if set(w).issubset(x)]
print(res)