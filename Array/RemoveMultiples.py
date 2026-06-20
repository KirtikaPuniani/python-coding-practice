#Remove multiples elements from a list

arr = [1,2,3,4,5,6,7,8,9,10]
def removeMultiples(arr):
    new_arr = []
    for a in arr:
        if a % 2 != 0:
            new_arr.append(a)
    return new_arr

print(removeMultiples(arr))