def cadena_tail(matriz, i, j, horizontal = '', vertical = '', flag = False, copy_j = None):
    if copy_j is None:
        copy_j = j
    if flag is False:
        if j == -1:
            return cadena_tail(matriz, i, copy_j, horizontal, vertical, flag = True)
        horizontal = horizontal + matriz[i][j]
        return cadena_tail(matriz, i, j-1, horizontal, vertical, flag, copy_j)
    else:
        if i == len(matriz):
            return 'Horizontal izquierda: ' + horizontal + '\nVertical abajo: ' + vertical
        vertical = vertical + matriz[i][j]
        return cadena_tail(matriz, i+1, j, horizontal, vertical, flag, copy_j)
    
    
def cadena_non_tail(matriz, i, j, direccion = None):
    if direccion is None:
        return 'Horizontal izquierda: ' + cadena_non_tail(matriz, i, j, True) + '\nVertical abajo: ' + cadena_non_tail(matriz, i, j, False)
    if direccion is True:
        if j == -1:
            return ''
        return matriz[i][j] + cadena_non_tail(matriz, i, j-1, True)
    if direccion is False:
        if i == len(matriz):
            return ''
        return matriz[i][j] + cadena_non_tail(matriz, i+1, j, False)
    

matriz = [
['C', 'A', 'S', 'A'],
['L', 'O', 'S', 'O'],
['P', 'E', 'R', 'O']
]
i, j = 1, 2

print(cadena_tail(matriz, i, j))
print()
print(cadena_non_tail(matriz, i, j))
