#Remove empty tuples from a list

arr = [1,2,3,4,(),5,6,(),7,8,9,(),10]
result = []

def removemptyTuples():
    for a in arr:
        if a:
            result.append(result)
    return result

print(removemptyTuples())