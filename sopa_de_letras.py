

def sopa_de_letras(matriz, palabra: str, ubicacion, actual=None, idx=0, i=None, j=None, n=None, ruta_actual=[]):
    if actual is None:
        palabra = palabra.upper()
        actual = palabra[idx]
    if i is None:
        i = ubicacion[0]
        j = ubicacion[1]
        n = len(matriz)
    if i < 0 or i >= n or j < 0 or j >= n:
        return ruta_actual
    opcion_actual = matriz[i][j]
    print(opcion_actual)
    print(actual)
    if opcion_actual is None:
        return
    if opcion_actual != actual:
        return
    if opcion_actual == actual:
        idx += 1
        actual = palabra[idx]
        
    ruta_actual.append((i, j))
    matriz[i][j] = None
    direcciones = [(1,0),(-1,0),(0,1),(0,-1)]
    for f, c in direcciones:
        sopa_de_letras(matriz, palabra, ubicacion, actual, idx, i+f, j+c, n, ruta_actual)
    ruta_actual.pop()
    matriz[i][j] = opcion_actual
    
    


print(sopa_de_letras([['A','V','O','Z','X','E'],
                      ['A','V','O','N','O','N'],
                      ['A','V','O','Q','M','P'],
                      ['A','V','T','X','E','Q'],
                      ['A','E','S','B','H','L'],
                      ['A','N','A','G','A','']], 'nomehaganesto', (1,3)))