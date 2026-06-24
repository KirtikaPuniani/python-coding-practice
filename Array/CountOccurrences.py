#Count occurrences of an element in a list

arr = [1,2,3,4,2,3,5,6,7,8,7,8,9,8,9,6,7,5]

def countOccurrences(arr, target):
    count = 0
    for a in arr:
        if a == target:
            count += 1
    return count
x = countOccurrences(arr, 8)
print(x)






#count occurences for all elements in the list
def countOccurrences(arr):
    counts = {}

    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    return counts

print(countOccurrences(arr))
