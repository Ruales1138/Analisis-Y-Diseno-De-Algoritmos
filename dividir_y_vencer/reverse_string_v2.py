def reverse(string, start = None, end = None):
    if start is None:
        start = 0
        end = len(string)-1
    if start == end:
        return string[start]
    mid = (start + end) // 2
    left = reverse(string, start, mid)
    right = reverse(string, mid+1, end)
    return right + left

print(reverse("abcd")) # → "dcba"
print(reverse("a")) # → "a"