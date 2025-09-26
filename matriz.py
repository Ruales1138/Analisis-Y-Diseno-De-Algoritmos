def suma_matriz(fila, columna, i=0, j=0, matriz=[]):
    if j == 0:
        matriz.append([])
    if j == len(columna):
        return
    
    
    print(matriz)
    fila_v, columna_v = validar(matriz)
    print(fila_v, columna_v)
    return matriz

def validar(matriz):
    sumas_columnas = []
    sumas_filas = []
    suma = 0
    for fila in matriz:
        sumas_columnas.append(sum(fila))
    for i in range(len(matriz[0])):
        for j in range(len(matriz)):
            suma += matriz[j][i]
        sumas_filas.append(suma)
        suma = 0
    return sumas_filas, sumas_columnas
    
            
print(suma_matriz([5,4,3], [11,20,10]))
print(suma_matriz([14,12,13], [15,25,21]))
print(suma_matriz([75,51,36,67,96], [66,66,66,62,65]))