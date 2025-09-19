def rutas_posibles(matriz, actual, ruta_actual=[], rutas=[]):
    i, j = actual
    
    actual_valor = matriz[actual[0]][actual[1]]
    if actual_valor == 'B':
        ruta_actual.append(actual)
        copia = ruta_actual.copy()
        rutas.append(copia)
        ruta_actual.pop()
        return rutas
    if actual[0] + 1 < len(matriz):
        siguiente = (actual[0]+1, actual[1])
        if actual_valor != '#' and siguiente not in ruta_actual:
            ruta_actual.append(actual)
            rutas_posibles(matriz, siguiente)
            ruta_actual.pop()
    if actual[1] + 1 < len(matriz[0]):
        siguiente = (actual[0], actual[1]+1)
        if actual_valor != '#' and siguiente not in ruta_actual:
            ruta_actual.append(actual)
            rutas_posibles(matriz, siguiente)
            ruta_actual.pop()
    if actual[0] - 1 >= 0:
        siguiente = (actual[0]-1, actual[1])
        if actual_valor != '#' and siguiente not in ruta_actual:
            ruta_actual.append(actual)
            rutas_posibles(matriz, siguiente)
            ruta_actual.pop()
    if actual[1] - 1 >= 0:
        siguiente = (actual[0], actual[1]-1)
        if actual_valor != '#' and siguiente not in ruta_actual:
            ruta_actual.append(actual)
            rutas_posibles(matriz, siguiente)
            ruta_actual.pop()
    return rutas

def ruta_mas_corta(matriz, posicion):
    rutas = rutas_posibles(matriz, posicion)
    menor_len = float('inf')
    menor = None
    for ruta in rutas:
        if len(ruta) < menor_len:
            menor_len = len(ruta)
            menor = ruta
    return menor
        

print(ruta_mas_corta([[' ',' ',' ',' ',' '],
                      ['A','#',' ','#',' '],
                      [' ',' ',' ',' ','B'],
                      [' ','#',' ','#',' ']], (1,0)))