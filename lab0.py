import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = [random.randint(1, 10000) for _ in range(1000)]

arr1 = arr.copy()
arr2 = arr.copy()

start = time.time()
bubble_sort(arr1)
end = time.time()
print("Bubble Sort time:", end - start, "seconds")

start = time.time()
selection_sort(arr2)
end = time.time()
print("Selection Sort time:", end - start, "seconds")
