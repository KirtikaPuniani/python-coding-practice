#All pair combinations of 2 tuples
# When working with Python tuples, you might need to generate all possible pair combinations between two tuples. This operation is useful in areas such as data science, simulation, and game development.
# Example:
# Input : t1 = (7, 2), t2 = (7, 8) 
# Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)] 



#Using itertools.chain() + product()
# The combination of itertools.product() and itertools.chain() is the most concise and efficient approach to generate all pair combinations.
# product(): creates Cartesian products between tuples.
# chain(): merges the two product results into a single iterable.