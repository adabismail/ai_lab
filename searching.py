# ---------- Linear Search ----------
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i   # return index
    return -1          # not found


# ---------- Binary Search ----------
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # not found


# ---------- Demo ----------
arr = [1, 3, 5, 7, 9, 11, 13]

print("Linear Search for 7:", linear_search(arr, 7))
print("Binary Search for 7:", binary_search(arr, 7))
