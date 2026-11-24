#Comb Sort
# Comb Sort is an improvement over Bubble Sort that solves its main problem - small values near the end slowing down the sorting. 
# It works by comparing elements far apart using a gap, which keeps reducing until it becomes 1. This allows faster movement of small elements toward the beginning and large elements toward the end.

#How Comb Sort Works
    # Initialize the gap: Start with a large gap (usually len(arr) / 1.3), where 1.3 is the shrink factor found experimentally.
    # Compare and swap: Compare elements that are gap positions apart and swap if they’re out of order.
    # Shrink the gap: Reduce the gap by dividing it by 1.3 each pass until it becomes 1.
    # Final pass: When the gap is 1, the algorithm behaves like Bubble Sort to finish sorting.
    
    
def combSort(arr):
    n = len(arr)
    gap = n
    swapped = True
    
    def getNextGap(gap):
        gap = int((gap * 10) / 13)
        return 1 if gap < 1 else gap
    
    while gap != 1 or swapped:
        gap = getNextGap(gap)
        swapped = False

        for i in range(0, n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True

arr = [8, 4, 1, 3, -44, 23, -6, 28, 0]
combSort(arr)

print(*arr)


# Explanation:
    # getNextGap(gap): Shrinks the gap by 1.3 and ensures it doesn’t go below 1.
    # combSort(arr): Sorts array using gradually reducing gaps.
    # while gap != 1 or swapped: Continues until array is sorted (gap = 1 and no swaps).
    # if arr[i] > arr[i + gap]: Swaps out-of-order elements at gap distance.
    # combSort(arr) & print(*arr): Sorts and prints the final sorted array.