import random
import time

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# === MAIN PROGRAM ===
# Generate a random list of 1000 integers
size = 1000
arr = [random.randint(1, 10000) for _ in range(size)]

# Make two copies (so both algorithms sort the same numbers)
arr_bubble = arr.copy()
arr_selection = arr.copy()

print("Original array (first 20 elements):", arr[:20])

# Time Bubble Sort
start = time.time()
bubble_sorted = bubble_sort(arr_bubble)
end = time.time()
print("\nBubble Sort time:", round(end - start, 4), "seconds")
print("Bubble Sort result (first 20 elements):", bubble_sorted[:20])

# Time Selection Sort
start = time.time()
selection_sorted = selection_sort(arr_selection)
end = time.time()
print("\nSelection Sort time:", round(end - start, 4), "seconds")
print("Selection Sort result (first 20 elements):", selection_sorted[:20])

