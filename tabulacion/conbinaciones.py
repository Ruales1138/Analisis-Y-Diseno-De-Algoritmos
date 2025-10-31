def conbinaciones(n: int):
    lista_letras = ['a', 'e', 'i', 'o', 'u']
    matriz = []
    fila = []
    for num in range(len(lista_letras)+1):
        fila.append(num)
    for _ in range(n+1):
        matriz.append(fila.copy())
    i = 1
    j = 1
    while i <= n:
        matriz[i][j] = matriz[i][j] ** i
        if j == len(lista_letras):
            i += 1
            j = 1
            continue
        j += 1
    for fila in matriz:
        print(fila)
    return matriz[-1][-1]

print(conbinaciones(4))