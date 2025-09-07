def longestNiceSubstring(s: str) -> str:
    def helper(start: int, end: int) -> str:
        if end - start < 2:
            return ""
        
        # Construir el conjunto de caracteres en este rango SIN slicing
        chars = set()
        for i in range(start, end):
            chars.add(s[i])
        
        # Buscar el primer carácter que no tiene su contraparte
        for i in range(start, end):
            c = s[i]
            if c.swapcase() not in chars:
                left = helper(start, i)
                right = helper(i + 1, end)
                if len(left) >= len(right):
                    return left
                else:
                    return right
        
        # Si todos tienen su contraparte, este rango es agradable
        return s[start:end]
    
    return helper(0, len(s))



print(longestNiceSubstring("YazaAay"))  # "aAa"
print(longestNiceSubstring("Bb"))       # "Bb"
print(longestNiceSubstring("c"))        # ""
print(longestNiceSubstring("dDzeE"))    # "dD"
