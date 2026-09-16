#Scraping and Finding ordered words in a dictionary
#An ordered word is a word in which the letters appear in alphabetical order. eg: abbey -> ordered and geeks -> not ordered


import requests 
url = 'https://www.puzzlers.org/pub/wordlists/unixdict.txt'
fd = requests.get(url)          #Download word list from URL
c1 = fd.content.decode('utf-8').split()[16:]           #Decode, split into words, skip first 16 entries

for word in c1:
    if len(word) < 3:
        continue
    if all(ord(word[i]) <= ord(word[i+1]) for i in range(len(word)-1)):           #check if letter are in alphabetical order
        print(f"{word}: Word is ordered")
        
        
##Approach
# 1. Scraping the dictioanry
#       - Fetch the content from the URL using the requests library
#       - Decode the UTF-8 content into a trinh
#       - Spliot the string into a list of words

#2. Finding ordered words
#       - Traverse the list of words
#       - Compare ASCII values of adjacent chars in each word
#       - If all chars are in alphabetical order, the word is ordered
#       - Otherwise skip it