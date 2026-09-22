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
output = list(map(lambda n: (n, n**3), tuple))    #lambda n, defines an anonymous function to create tuples of (number, cube). Map function applies the lambda to each element of numbers. List converts the result of map to a list
print(output)


#Using zip
tuple = [1,3,5,7,9]
output = list(zip(tuple, [n**3 for n in tuple]))       #[n**3 for n in tuple] generates a list of cubes. Zip(tuple, cubes) pairs each number with its cube. List function converts the pairs into A list of tuples
print(output)



#Using for loop with append