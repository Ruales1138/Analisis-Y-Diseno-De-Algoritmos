from collections import Counter

def remove_duplicate(string):
    char_count = Counter(string)
    current_ans = []
    current_set = set()
    for char in string:
        char_count[char] -= 1
        if char in current_set:
            continue
        while current_ans and char < current_ans[-1] and char_count[current_ans[-1]] > 0:
            current_set.remove(current_ans[-1])
            current_ans.pop()
        current_ans.append(char)
        current_set.add(char)
    return ''.join(current_ans)

print(remove_duplicate('bcabc')) # -> abc
print(remove_duplicate('cbacdcbc')) # -> acdb
print(remove_duplicate('bacbcacc')) # -> abc
