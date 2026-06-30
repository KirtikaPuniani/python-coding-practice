#Print duplicates from a list of integers

arr = [1,2,3,4,3,4,5,6,4,5,6,4,5,6,7,8,9,10,10,10]

def duplicateElements(arr):
    count = {}
    for a in arr:
        if a in count:
            count[a] += 1
        else:
            count[a] = 1
    
    for key, value in count.items():
        if value > 1:
            print(key)
            
duplicateElements(arr)