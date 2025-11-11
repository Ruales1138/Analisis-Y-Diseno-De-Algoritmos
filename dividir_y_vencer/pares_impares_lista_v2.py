def count(list, start=None, end=None):
    if start is None:
        start = 0
        end = len(list)-1
    if start == end:
        num = list[start]
        if num % 2 == 0:
            return (num, 1, 0)
        else:
            return (num, 0, 1)
    mid = (start + end) // 2
    left = count(list, start, mid)
    right = count(list, mid+1, end)
    sum = left[0] + right[0]
    even = left[1] + right[1]
    odd = left[2] + right[2]
    return (sum, even, odd)

print(count([1,2,3,4,5,6])) # -> (21, 3, 3)