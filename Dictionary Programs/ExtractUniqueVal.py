#Extract unique values dictionary values



#Using set and sum
d = {'gfg' : [5,6,7,8],
     'is' : [10,11,7,5], 
     'best' : [6,12,10,8], 
     'for' : [1,2,5]}
res = list(set(sum(d.values(), [])))      #data.values(): fetches all value lists.
#sum(..., []): flattens nested lists by concatenation.
#set(): removes duplicate elements.
print(res)




list(): converts the set into a list.