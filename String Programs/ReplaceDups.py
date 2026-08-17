#Replace duplicate occurence in string
#Replace only duplicate occurences of certain words in a string that is, replace a word from its second occurence onwards, while keeping its first occurence unchanged.
#eg: I/P s = 'Gfg is best. Gfg also has Classes now. Classes help understand better.' O/P: 'Gfg is best. It also has Classes now. They help understand better.'


#Using list comprehension and set
s = 'Gfg is best. Gfg also has Classes now. Classes help understand better.'
rep = {'Gfg': 'It', 'Classes': 'They'}
seen = set()
result = [rep[word] if word in rep and word in seen else(seen.add(word) or word) for word in s.split()]
s2 = ' '.join(result)
print(s2)




#Using regular expression
import re
s = 'Gfg is best. Gfg also has Classes now. Classes help understand better.'
rep = {'Gfg': 'It', 'Classes': 'They'}
pattern = r'\b(' + '|'.join(re.escape(k) for k in rep.keys()) + r')\b'
seen = set()
def repDup(m):
    word = m.group(1)
    if word in seen:
        return rep[word]
    seen.add(word)
    return word
result = re.sub(pattern, repDup, s)
print(result)