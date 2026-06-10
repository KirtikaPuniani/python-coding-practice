#Using reverse()
list = [10, 20, 30, 40, 50, 60]
list.reverse()
print(list)
#The reverse() method reverses the elements of the list in place, meaning it modifies 
# the original list. After calling reverse(), the order of the elements in the list is reversed.


#Using list slicing
list = [10, 20, 30, 40, 50, 60]
reversed_list = list[::-1]
print(reversed_list)
#The slicing syntax list[::-1] creates a new list that is a reversed version of the 
# original list. The [::-1] slice notation means to take the elements of the list in 
# reverse order. This does not modify the original list, but instead creates a new 
# list with the elements in reverse order.