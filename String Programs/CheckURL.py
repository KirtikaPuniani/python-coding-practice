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