#Bitonic Sort

# A sequence is bitonic if it first increases and then decreases. Formally, an array arr[0..n-1] is bitonic if there exists an index i (0 ≤ i ≤ n−1) such that:

# x0 <= x1 …..<= xi  and  xi >= xi+1….. >= xn-1
# A fully increasing or fully decreasing sequence is also considered bitonic.
# Any rotation of a bitonic sequence remains bitonic.
# Bitonic Sort is a parallel sorting algorithm that works efficiently when the number of elements is a power of 2.

# How Bitonic Sort Works
    # It mainly works in two steps:
    # Form a bitonic sequence: divide the array into two halves- one sorted in ascending order and the other in descending order.
    # Merge: compare and swap elements to form smaller bitonic sequences until the entire array is sorted.




def bitonicMerge(a, low, cnt, dire):
    if cnt > 1:
        k = cnt // 2
        for i in range(low, low + k):
            if (dire == 1 and a[i] > a[i + k]) or (dire == 0 and a[i] < a[i + k]):
                a[i], a[i + k] = a[i + k], a[i]
        bitonicMerge(a, low, k, dire)
        bitonicMerge(a, low + k, k, dire)

def bitonicSort(a, low, cnt, dire):
    if cnt > 1:
        k = cnt // 2
        bitonicSort(a, low, k, 1)   
        bitonicSort(a, low + k, k, 0)  
        bitonicMerge(a, low, cnt, dire)

def sort(a, N, up):
    bitonicSort(a, 0, N, up)

a = [3, 7, 4, 8, 6, 2, 1, 5]
n = len(a)
up = 1 

sort(a, n, up)
print(*a)


# Explanation:

# bitonicSort(a, low, cnt, dire): recursively divides the array and sorts halves in opposite directions to form a bitonic sequence.
# bitonicMerge(a, low, cnt, dire): compares and swaps elements based on direction to merge the bitonic sequence into sorted order.
# k = cnt // 2: splits the current sequence into two equal halves.
# dire == 1 / 0: determines sorting order - 1 for ascending, 0 for descending.
# sort(a, N, up): wrapper function that initiates bitonic sorting on the full array.