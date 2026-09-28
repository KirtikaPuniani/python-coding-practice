#Adding tuple to list and vice-versa


#Using extend and '+' operator
a = [1,2,3]
b= (4,5)
a.extend(b)       #add tuple to list 'a'. adds each element of b to a.
print(a)
x = tuple(a) + b     #add list to tuple 'b'. we can't do simple a + b because the type of variables is diff, one is tuple and other is list so we have to type cast the variable.
print(x)



#Using * operator and append
a = [1,2,3]
b= (4,5)
a.append(b)
print(a)
x = (*a, *b)
print(x)


#Using insert and list comprehension
#Insert function places the tuple at a specific position. List comprehension creates a new tuple when merging
a = [1,2,3]
b= (4,5)
a.insert(len(a), b)         #adds b at the end of a and tuple(x for x in a) creates a tuple from a, then + tuple(b) merges it with b
print(a)
x = tuple(x for x in a) + tuple(b)
print(x)



#Using list ans tuple
a = [1,2,3]
b= (4,5)
a.extend(list(b))
print(a)
temp_list = list(b)
temp_list.extend(a)
x = tuple(temp_list)
print(x)