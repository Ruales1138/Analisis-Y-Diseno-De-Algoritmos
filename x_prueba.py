def longestSubstring(s: str, k: int) -> int:
    # Caso base: si la cadena es muy corta no puede haber solución
    if len(s) < k:
        return 0

    # Revisar cuántas veces aparece cada letra
    conteo = {}
    for letra in s:
        if letra not in conteo:
            conteo[letra] = 0
        conteo[letra] += 1

    # Si todos los caracteres aparecen al menos k veces, la cadena completa sirve
    cumple = True
    for letra in conteo:
        if conteo[letra] < k:
            cumple = False
            break
    if cumple:
        return len(s)

    # Si hay algún caracter que no cumple, lo usamos como separador
    for letra in conteo:
        if conteo[letra] < k:
            # Cortamos la cadena en pedazos donde aparezca esa letra
            partes = s.split(letra)
            # Revisamos cada parte por separado y nos quedamos con la mayor
            mejor = 0
            for parte in partes:
                longitud = longestSubstring(parte, k)
                if longitud > mejor:
                    mejor = longitud
            return mejor

    return 0


print(longestSubstring("aaabb", 3))   # ➝ 3 ("aaa")
print(longestSubstring("ababbc", 2))  # ➝ 5 ("ababb")
