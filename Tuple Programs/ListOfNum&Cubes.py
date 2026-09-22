#Create a list of tuples with numbers and their cubes
#Given a list of numbers, the task is to create a list of tuples where each tuple contains a number and its cube.
# Input: [1, 2, 3]
# Output: [(1, 1), (2, 8), (3, 27)]



#Using list comprehension
tuple = [1,3,5,7,9]
output = [(n, n**3) for n in tuple]       #for n in tuple iterates over each element n in the list and creayes a tuple with the number and its cube. Square brackets [] collect all tuples into a list
print(output)


#Using map with lambda
tuple = [1,3,5,7,9]
output = list(map(lambda n: (n, n**3), tuple))
print(output)