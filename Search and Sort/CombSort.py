#Comb Sort
# Comb Sort is an improvement over Bubble Sort that solves its main problem - small values near the end slowing down the sorting. 
# It works by comparing elements far apart using a gap, which keeps reducing until it becomes 1. This allows faster movement of small elements toward the beginning and large elements toward the end.

#How Comb Sort Works
    # Initialize the gap: Start with a large gap (usually len(arr) / 1.3), where 1.3 is the shrink factor found experimentally.
    # Compare and swap: Compare elements that are gap positions apart and swap if they’re out of order.
    # Shrink the gap: Reduce the gap by dividing it by 1.3 each pass until it becomes 1.
    # Final pass: When the gap is 1, the algorithm behaves like Bubble Sort to finish sorting.