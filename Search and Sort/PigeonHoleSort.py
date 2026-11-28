#Pigeon Hole Sort
#Pigeonhole Sort is a sorting algorithm that is suitable for sorting lists of elements where the number of elements and the range of possible key values are approximately the same. It works by placing each element into a "hole" corresponding to its key value, and then collecting the elements from the holes in order.
#Pigeonhole Sort is a simple sorting algorithm used when the number of elements (n) and the range of possible values (k) are roughly the same. It works by placing each element into a "pigeonhole" (a slot based on its value) and then reading them back in sorted order.


# Working of Pigeonhole Sort
#     1. Find range:
#         Find the minimum (min) and maximum (max) values in the list.
#         Range = max - min + 1
#     2. Create pigeonholes: Create an array (list) of empty pigeonholes - one for each possible value in the range.
#     3. Distribute elements:
#         For each element in the list, place it in its corresponding pigeonhole using the formula:
#         index = element - min
#     4. Reconstruct sorted list: Traverse all pigeonholes in order, putting their elements back into the original list.


def pigeonhole_sort(a):
    mi, mx = min(a), max(a)
    size = mx - mi + 1
    holes = [0] * size

    for x in a:
        assert isinstance(x, int), "Only integers allowed"
        holes[x - mi] += 1

    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            a[i] = count + mi
            i += 1

a = [8, 3, 2, 7, 4, 6, 8]
pigeonhole_sort(a)
print(a)




# Explanation:
#     my_min, my_max = min(a), max(a): Finds smallest and largest elements.
#     holes = [0] * (my_max - my_min + 1): Creates pigeonholes for all possible values.
#     holes[x - my_min] += 1: Counts occurrences of each number.
#     for count in range(size): Iterates through pigeonholes.
#     a[i] = count + my_min: Fills array back in sorted order.







