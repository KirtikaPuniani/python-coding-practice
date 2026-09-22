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