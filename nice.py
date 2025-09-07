def nice(string: str, start = None, end = None):
    if start is None:
        start = 0
        end = len(string)
    if end - start <= 1:
        return ''
    chars = set()
    for i in range(start, end):
        chars.add(string[i])
    for i in range(start, end):
        if string[i].swapcase() not in chars:
            left = nice(string, start, i)
            right = nice(string, i+1, end)
            if len(left) >= len(right):
                return left
            else:
                return right
    return string[start:end]

print(nice("YazaAay")) # -> "aAa"
print(nice("Bb")) # -> "Bb"
print(nice("c")) # -> ""