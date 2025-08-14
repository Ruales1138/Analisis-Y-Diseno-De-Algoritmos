def separa_letras_tail(palabra: str, contador: list[int] = [0, 0], i: int = 0):
    if i == len(palabra):
        if contador[0] > contador[1]:
            return 'Vocales: ' + str(contador[0])
        else:
            return 'Consonantes: ' + str(contador[1])
    if palabra[i] in 'aeiou':
        contador[0] += 1
    else:
        contador[1] += 1
    return separa_letras_tail(palabra, contador, i+1)

def separa_letras_non_tail(palabra: str, contador: list[int] = [0, 0], i: int = 0):
    if i == len(palabra):
        return contador
    resultado = separa_letras_non_tail(palabra, contador, i+1)
    if palabra[i] in 'aeiou':
        contador[0] += 1
    else:
        contador[1] += 1
    if i == 0:
        if contador[0] > contador[1]:
            return 'Vocales: ' + str(contador[0])
        else:
            return 'Consonantes: ' + str(contador[1])


 
print(separa_letras_tail('aeiou'))
print(separa_letras_tail('aeisgfg', [0,0]))
print()
print(separa_letras_non_tail('aeiou'))
print(separa_letras_non_tail('aeisgfg', [0,0]))


