def cadena_non_tail(matriz, i, j, direccion=None):
    if direccion is None:
        return f'Horizontal izquierda: {cadena_non_tail(matriz, i, j, True)}\nVertical abajo: {cadena_non_tail(matriz, i, j, False)}'
    if direccion:
        if j == -1:
            return ''
        return matriz[i][j] + cadena_non_tail(matriz, i, j-1, direccion)
    else:
        if i == len(matriz):
            return ''
        return matriz[i][j] + cadena_non_tail(matriz, i+1, j, direccion)

matriz = [
['C', 'A', 'S', 'A'],
['L', 'O', 'S', 'O'],
['P', 'E', 'R', 'O']
]
i, j = 1, 2

print(cadena_non_tail(matriz, i, j)) # -> Horizontal izquierda: SOL
                                     #    Vertical abajo: SR