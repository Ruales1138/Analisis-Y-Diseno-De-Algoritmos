def caminos(m: int, n: int):
    matriz = []
    for _ in range(n):
        matriz.append([1]*(m))
    print(matriz)
    i = 1
    j = 1
    while i < n:
        print(i,j)
        matriz[i][j] = matriz[i-1][j] + matriz[i][j-1]
        if j == (m-1):
            i += 1
            j = 1
            continue
        j +=1
    for idx in range(len(matriz)):
        print(matriz[idx])
    return matriz[-1][-1]

print(caminos(6, 5))