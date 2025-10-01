def suma_matriz(fila, columna):
    matriz = []
    for _ in range(len(fila)):
        matriz.append([0]*len(fila))
    print(matriz)
    def recurcion(matriz, i=0, j=0, visitados=[]):
        #print(i,j)
        if i == len(fila):
            return True
        columna_v = sum(matriz[i])
        if columna_v == columna[i]:
            return True
        for n in range(1, 5):
            if n not in visitados:
                if j < len(columna):
                    matriz[i][j] = n
                    visitados.append(n)
                    print(matriz)
                    columna_v = sum(matriz[i])
                    print(columna_v, columna[i])
                    if columna_v == columna[i]:
                        print('----------')
                        respuesta = recurcion(matriz, i+1, 0)
                        if respuesta is True:
                            return True
                    if columna_v > columna[i]:
                        return True
                    if columna_v < columna[i]:
                        respuesta = recurcion(matriz, i, j+1)
                        if respuesta is True:
                            return True
                    if respuesta == True:
                        return
                    matriz[i][j] = 0
                    visitados.pop()
                # if j == len(columna):
                #     recurcion(matriz, i+1, 0)
    return recurcion(matriz)

def validar(matriz):
    sumas_columnas = []
    sumas_filas = []
    suma = 0
    for f in matriz:
        sumas_columnas.append(sum(f))
    for i in range(len(matriz[0])):
        for j in range(len(matriz)):
            suma += matriz[j][i]
        sumas_filas.append(suma)
        suma = 0
    return sumas_filas, sumas_columnas
    
print(suma_matriz([3,7], [5,5])) 
#print(suma_matriz([19,9,17], [11,18,16])) 
# print(suma_matriz([5,4,3], [11,20,10]))
# print(suma_matriz([14,12,13], [15,25,21]))
# print(suma_matriz([75,51,36,67,96], [66,66,66,62,65]))