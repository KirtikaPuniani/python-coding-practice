#Check for URL in a string
#We are given a string that may contain one or more URLs and our tast is to extract them efficiently. This is useful for web scraping, text processing and data validation.
#Eg: Input: s = "My Profile: https://www.geeksforgeeks.org/404.html/ in the portal of https://www.geeksforgeeks.org/"
#    Output: ['https://www.geeksforgeeks.org/404.html/', 'https://www.geeksforgeeks.org/']


#Using re.findall()
import re
s =  "My Profile: https://www.geeksforgeeks.org/404.html/ in the portal of https://www.geeksforgeeks.org/"
pattern = r'https?://\S+|www\.\S+'
print("URLs:", re.findall(pattern, s))
# Explanation:
# https?://\S+ matches URLs starting with http:// or https://.
# www\.\S+ matches URLs starting with www.
# findall(): returns all matches in a list.




#Using the urlparse
from urllib.parse import urlparse
s = "My Profile: https://www.geeksforgeeks.org/404.html/ in the portal of https://www.geeksforgeeks.org/"
s1 = s.split()
urls = []
for word in s1:
    parsed = urlparse(word)
    if parsed.scheme and parsed.netloc:
        urls.append(word)
print("URLs:", urls)
# Explanation:
# s.split(): function splits the string to words.
# urlparse(word): function checks each word to see if it has a valid scheme (http/https) and domain.
# URLs are added to url list using append() function.