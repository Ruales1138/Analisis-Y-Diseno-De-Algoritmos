def cadena_tail(matriz, i, j, horizontal='', vertical='', flag=False, copia_j=None):
    if copia_j is None:
        copia_j = j
    if not flag:
        if j == -1:
            return cadena_tail(matriz, i, copia_j, horizontal, vertical, True)
        return cadena_tail(matriz, i, j-1, horizontal+matriz[i][j], vertical, flag, copia_j)
    else:
        if i == len(matriz):
            return f'Horizontal izquierda: {horizontal}\nVertical abajo: {vertical}'
        return cadena_tail(matriz, i+1, j, horizontal, vertical+matriz[i][j], flag, copia_j)

matriz = [
['C', 'A', 'S', 'A'],
['L', 'O', 'S', 'O'],
['P', 'E', 'R', 'O']
]
i, j = 1, 2

print(cadena_tail(matriz, i, j)) # -> Horizontal izquierda: SOL
                                 #    Vertical abajo: SR