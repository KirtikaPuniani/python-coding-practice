#the task is to swap the first and last elements of the list without changing the 
# order of the remaining elements.

# Example:
# Input: [10, 20, 30, 40, 50]
# Output: [50, 20, 30, 40, 10]


#Using direct assignment
list = [10, 20, 30, 40, 50]
list[0], list[-1] = list[-1], list[0]
print(list)
#Explanation: lst[0] and lst[-1] returns the first and the last element of the list, we can simply swap them using 
# assignment operator.



#Using tuple variable
list = [10, 20, 30, 40, 50]
pair = list[0], list[-1]
list[0], list[-1] = pair
print(list)
#Explanation: We create a tuple variable pair that holds the first and last elements of the list and then we swap them 
# using assignment operator. 



#Using * operator
list = [10, 20, 30, 40, 50]
first, *middle, last = list
list[0], list[-1] = last, first
print(list)
#Explanation: We use the * operator to unpack the list into three variables: first, middle, and last. Then we swap the 
# first and last variables and assign them back to the list.