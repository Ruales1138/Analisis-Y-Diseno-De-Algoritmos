def binary_search(arr: list[int], target: int, left = None, right = None):
    if len(arr) == 0:
        return -1
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1
    mid = int((left + right) / 2)
    if arr[mid] == target:
        return mid
    if target < arr[mid]:
        right = mid - 1
    if target > arr[mid]:
        left = mid + 1
    return binary_search(arr, target, left, right)
    

print(binary_search([1, 3, 5, 7, 9], 5))   # → 2
print(binary_search([1, 3, 5, 7, 9], 10))   # → -1
print(binary_search([1, 3, 5, 7, 9], 1))   # → 0
print(binary_search([], 3))  # → -1
print(binary_search([42], 42))   # → 0