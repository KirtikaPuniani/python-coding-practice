#Find the n largest elements in an array

arr = [1, 3, 5, 2, 4, 7, 6, 9, 8, 10]
def nLargest(arr, n):
    if n > len(arr):
        return "n is greater than the length of the array"
    
    largest_elements = sorted(arr, reverse=True)[:n]
    return largest_elements

x = nLargest(arr, 3)
print(x)