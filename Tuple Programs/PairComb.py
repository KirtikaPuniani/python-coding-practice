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
