#Using in Statement
list = [1,3,4,5,6,2,6,7,8,9,0,10,23,45,67,89,90]

if 50 in list:
    print("Element is present in the list")
else:
    print("Element is not present in the list")
    
    

#Using a loop to check for the presence of an element in the list
list = [1,3,4,5,6,2,6,7,8,9,0,10,23,45,67,89,90]
key = 50
found = False

for i in list:
    if i == key:
        flag = True
        break
if found:
    print("Element is present in the list")
else:
    print("Element is not present in the list")
    
    

#Using any() function to check for the presence of an element in the list
list = [1,3,4,5,6,2,6,7,8,9,0,10,23,45,67,89,90]
flag = any(x == 30 for x in list)

if flag:
    print("Element exists in the list")
else:
    print("Element does not exist")

# Explanation:
# any(x == 30 for x in a): Checks each element in the list a to see if it equals 30. returns true if any element matches.
# flag: Stores the result (True if 30 is found, otherwise False).






#Using count() method to check for the presence of an element in the list
list = [1,3,4,5,6,2,6,7,8,9,0,10,23,45,67,89,90]
if list.count(30) > 0:
    print("Element exists in the list")
else:
    print("Element does not exist in the list")