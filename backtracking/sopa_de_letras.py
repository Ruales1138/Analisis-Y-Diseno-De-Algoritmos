def encontrar_primero(matriz, palabra: str):
    primero = palabra[0].upper()
    primeros_lista = []
    for i, fila in enumerate(matriz):
        if primero in fila:
            primeros_lista.append((i, fila.index(primero)))
    for opcion in primeros_lista:
        if sopa_de_letras(matriz, palabra, opcion):
            return True
    return False

def sopa_de_letras(matriz, palabra: str, ubicacion, actual=None, idx=0, i=None, j=None, n=None, ruta_actual=[]):
    if actual is None:
        palabra = palabra.upper()
        actual = palabra[idx]
    if i is None:
        i = ubicacion[0]
        j = ubicacion[1]
        n = len(matriz)
    if i < 0 or i >= n or j < 0 or j >= n or len(ruta_actual) == len(palabra):
        palabra_encontrada = ''.join(ruta_actual)
        if palabra_encontrada == palabra.upper():
            return True
        else:
            return False
    opcion_actual = matriz[i][j]
    if opcion_actual is None or opcion_actual != actual:
        return
    if opcion_actual == actual and idx < len(palabra)-1:
        idx += 1
        actual = palabra[idx]
    ruta_actual.append(opcion_actual)
    matriz[i][j] = None
    direcciones = [(1,0),(-1,0),(0,1),(0,-1)]
    for f, c in direcciones:
        if sopa_de_letras(matriz, palabra, ubicacion, actual, idx, i+f, j+c, n, ruta_actual):
            return True
    ruta_actual.pop()
    matriz[i][j] = opcion_actual
    return False
    
print(encontrar_primero([['A','V','O','Z','X','E'],
                        ['A','V','O','N','O','N'],
                        ['A','V','O','Q','M','P'],
                        ['A','V','T','X','E','Q'],
                        ['A','E','S','B','H','L'],
                        ['A','N','A','G','A','Q']], 'nomehaganesto')) # 1,3