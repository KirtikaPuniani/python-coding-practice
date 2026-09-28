#All pair combinations of 2 tuples
# When working with Python tuples, you might need to generate all possible pair combinations between two tuples. This operation is useful in areas such as data science, simulation, and game development.
# Example:
# Input : t1 = (7, 2), t2 = (7, 8) 
# Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)] 



#Using itertools.chain() + product()
# The combination of itertools.product() and itertools.chain() is the most concise and efficient approach to generate all pair combinations.
# product(): creates Cartesian products between tuples.
# chain(): merges the two product results into a single iterable.
from itertools import chain, product
x = (4, 5)
y = (7, 8)
res = list(chain(product(x, y),product(y, x)))       #product(x, y) creates all forward pair combinations.   and     product(y, x) creates all reverse pair combinations.
#chain(product(...), product(...)): combines both forward and reverse combinations into a single iterable
#list(chain(...)): converts that combined iterable into a list, storing all pair combinations in output
print(str(res))




#Using list comprehensions
x = (4, 5)
y = (7, 8)
output = [(a, b) for a in x for b in y] + \
      [(a, b) for a in y for b in x]
#[(a, b) for a in x for b in y]: generates all forward pairs (elements from the first tuple combined with the second)
#[(a, b) for a in y for b in x]: generates all reverse pairs (elements from the second tuple combined with the first)
print(str(output))



#Using itertools.product()
import itertools
x = (4, 5)
y = (7, 8)
output = [(a, b) for a in x for b in y] + \
      [(a, b) for a in y for b in x]
# [(a, b) for a in x for b in y]: generates all forward pair combinations.
# [(a, b) for a in y for b in x]: generates all reverse pair combinations.
print(str(output))



#Using nested loop
x = (4, 5)
y = (7, 8)
output = []
for element_1 in x:
    for element_2 in y:
        output.append((element_1, element_2))       #Adds forward pair
        output.append((element_2, element_1))       #Adds reverse pair
print(output)