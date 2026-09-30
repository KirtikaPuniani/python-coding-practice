#Sort a List of Tuples by Second Item


#Using itemgetter
from operator import itemgetter 
a = [(7, 5), (3, 8), (2, 6)]  
res = sorted(a, key=itemgetter(1))
print(res)