#Using clear() method to clear a list in python
list = [1,3,4,5,6,2,6,7,8,9,0,10,23,45,67,89,90]
list.clear()
print(list)
#clear removes all the items from the list, leaving it empty. 
# The list itself still exists, but it contains no elements.


#Using del a[:]
list = [1,3,4,5,6,2,6,7,8,9,0,10,23,45,67,89,90]
del list[:]
print(list)
#del a[:] deletes all the elements in the list a, leaving it empty. 
# The list itself still exists, but it contains no elements.


#Using a loop with pop()
list = [1,3,4,5,6,2,6,7,8,9,0,10,23,45,67,89,90]
while list:
    list.pop()
print(list)
#This code uses a while loop to repeatedly call the pop() method on the list until it
# is empty. The pop() method removes the last element from the list, so this 
# effectively clears the list one element at a time.