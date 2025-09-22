def posibles_sumas(matriz, target, fila=0, columna=0, ruta_actual=[], rutas=[]):
    if fila < 0 or fila >= len(matriz) or columna < 0 or columna >= len(matriz[0]):
        return rutas
    n_actual = matriz[fila][columna]
    if n_actual is None:
        return rutas
    if target - n_actual < 0:
        return rutas
    if target - n_actual == 0:
        ruta_actual.append(n_actual)
        copia = ruta_actual.copy()
        rutas.append(copia)
        ruta_actual.pop()
        return rutas
    if target - n_actual > 0:
        ruta_actual.append(n_actual)
        matriz[fila][columna] = None
        direcciones = [(1,0),(-1,0),(0,1),(0,-1)]
        for i, j in direcciones:
            posibles_sumas(matriz, target-n_actual, fila+i, columna+j, ruta_actual, rutas)
        matriz[fila][columna] = n_actual
        ruta_actual.pop()
    return rutas
    
print(posibles_sumas([[2,3,3,2],
                      [1,5,-4,-10],
                      [0,-5,9,5]], 8))
