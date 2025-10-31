def mejor_camino(matriz):
    matriz_2 = []
    for _ in range(len(matriz)+1):
        matriz_2.append([0]*(len(matriz[0])+1))
    print(matriz_2)
    i = 1
    j = 1
    while i <= len(matriz):
        print(i,j)
        matriz_2[i][j] = matriz[i-1][j-1] + max(matriz_2[i-1][j], matriz_2[i][j-1])
        if j == len(matriz_2[0])-1:
            i += 1
            j = 1
            continue
        j += 1
    for fila in matriz_2:
        print(fila)
    return matriz_2[-1][-1]



print(mejor_camino([[1,1,1],[2,10,20],[1,0,2]]))