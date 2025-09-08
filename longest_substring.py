def longest_substring(string, k, start = None, end = None):
    if start is None:
        start = 0
        end = len(string)
    if end - start < k:
        return 0
    count = {}
    for i in range(start, end):
        char = string[i]
        if char not in count:
            count[char] = 0
        count[char] += 1
    for i in range(start, end):
        char = string[i]
        if count[char] < k:
            left = longest_substring(string, k, start, i)
            right = longest_substring(string, k, i+1, end)
            return max(left, right)
    return end - start


print(longest_substring("aaabb", 3)) # -> 3
print(longest_substring("ababbc", 2)) # -> 5