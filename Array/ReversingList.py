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



#Using reversed()
a = [10, 20, 30, 40, 50, 60]
rev = list(reversed(a))
print(rev)
#The reversed() function returns an iterator that yields the elements of the list in
# reverse order. By passing the original list to the reversed() function and then
# converting the result to a list, we get a new list that contains the elements in
# reverse order. This does not modify the original list, but instead creates a new




#Using a loop to reverse a list
list = [10, 20, 30, 40, 50, 60]
i, j = 0, len(list) - 1
while i < j:
    list[i], list[j] = list[j], list[i]
    i += 1
    j -= 1
print(list)
#This code uses a while loop to swap elements from the start and end of the list until
# it reaches the middle. The variables i and j are used to keep track of the indices
# of the elements being swapped. After the loop completes, the list is reversed in place.