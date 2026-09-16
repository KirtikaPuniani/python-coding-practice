#Scraping and Finding ordered words in a dictionary
#An ordered word is a word in which the letters appear in alphabetical order. eg: abbey -> ordered and geeks -> not ordered


import requests 
url = 'https://www.puzzlers.org/pub/wordlists/unixdict.txt'
fd = requests.get(url)
c1 = fd.content.decode('utf-8').split()[16:]

for word in c1:
    if len(word) < 3:
        continue
    if all(ord(word[i]) <= ord(word[i+1]) for i in range(len(word)-1)):
        print(f"{word}: Word is ordered")