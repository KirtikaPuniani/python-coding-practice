#remove empty list from a list

arr = [1,2,3,[],4,5,6,[],7,8,9,10]
def removeEmptyList(arr):
    return [a for a in arr if a != []]

print(removeEmptyList(arr))