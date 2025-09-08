def max_min(nums, start = None, end = None):
    if start is None:
        start = 0
        end = len(nums)-1
    if start == end:
        return (nums[start], nums[start])
    mid = (start + end) // 2
    left = max_min(nums, start, mid)
    right = max_min(nums, mid+1, end)
    return (min(left[0], right[0]), max(left[1], right[1]))

print(max_min([3, 7, 2, 9])) # → (2, 9)
print(max_min([5])) # → (5, 5)
print(max_min([38, 27, 43, 3, 9, 82, 10])) # -> (3, 82)