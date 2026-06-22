#Remove multiples elements from a list

arr = [1,2,3,4,5,6,7,8,9,10]
remove = [2,4,6,7,10]
def removeMultiples(arr):
    for a in remove:
        if a in arr:
            arr.remove(a)
    return arr

print(removeMultiples(arr))