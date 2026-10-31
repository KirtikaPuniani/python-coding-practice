#Shell Sort Algorithm
#Shell Sort is an in-place comparison-based sorting algorithm that generalizes insertion sort to allow the exchange of items that are far apart. The idea is to arrange the list of elements so that, starting anywhere, taking 
# every hth element produces a sorted list. Such a list is said to be h-sorted. It can also be thought of as a generalization of sorting by exchange (bubble sort) or sorting by insertion (insertion sort). The method starts by 
# sorting pairs of elements far apart from each other, then progressively reducing the gap between elements to be compared. Starting with far apart elements can move some out-of-place elements into position faster than a 
# simple nearest neighbor exchange.

# Algorithm Steps
    # 1. Initialize the gap as half the length of the array (n/2).
    # 2. Divide the array into smaller sublists, each separated by the gap.
    # 3. Perform insertion sort within these sublists.
    # 4. Reduce the gap size and repeat sorting until the gap becomes 0.
    # 5. Stop when the array is completely sorted.


# Working Example:
# Let’s take a small list for example: [9, 1, 5, 3]. Below is the step-by-step process:
# Initial list: [9, 1, 5, 3], Number of elements = 4 → start with gap = 2.

# Pass 1 (gap = 2):
#     Compare arr[0] (9) and arr[2] (5): since 9 > 5 → swap → [5, 1, 9, 3]
#     Compare arr[1] (1) and arr[3] (3): since 1 < 3 → no swap → Result after gap=2: [5, 1, 9, 3]
#     Reduce gap: gap = 1 (regular insertion sort step)

# Pass 2 (gap = 1):
#     Compare arr[1] (1) with arr[0] (5): 1 < 5 → swap → [1, 5, 9, 3]
#     Compare arr[2] (9) with arr[1] (5): 9 > 5 → no swap
#     Compare arr[3] (3) with arr[2] (9): 3 < 9 → swap → [1, 5, 3, 9]
#     Compare arr[2] (3) with arr[1] (5): 3 < 5 → swap → [1, 3, 5, 9]. Result after gap=1: [1, 3, 5, 9] (sorted).
