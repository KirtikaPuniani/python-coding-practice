#Print all even numbers in the given range

arr = range(1, 25)

def evenRange(arr):
    even_num = []
    for a in arr:
        if a % 2 == 0:
            even_num.append(a)
    return even_num

x = evenRange(arr)
print("Even numbers in the given range:", x)