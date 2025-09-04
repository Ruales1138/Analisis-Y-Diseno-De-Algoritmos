def longest_substring(string, num):
    count = {}
    if num > len(string):
        return 0
    for letter in string:
        if letter not in count:
            count[letter] = 1
        else:
            count[letter] += 1
    flag = True
    for key, value in count.items():
        print(key, value)
        if value < num:
            flag = False
            break
    if flag:
        return len(string)
    else:
        return []

print(longest_substring("aaabb", 3))   # ➝ 3 ("aaa")
print(longest_substring("ababbc", 2))  # ➝ 5 ("ababb")