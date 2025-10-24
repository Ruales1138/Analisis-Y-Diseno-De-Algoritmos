def mochila(n: int, w: int, weights: list, values: list):
    matriz = []
    for _ in range(n+1):
        matriz.append([0]*(w+1))
    i = 1
    j = 1
    while i <= n:
        current_weight = weights[i-1]
        current_value = values[i-1]
        if current_weight > j:
            matriz[i][j] = matriz[i-1][j]
        if current_weight <= j:
            matriz[i][j] = max(current_value + matriz[i-1][j-current_weight], matriz[i-1][j])
        if j == w:
            i += 1
            j = 1
            continue
        j += 1
    for i in range(len(matriz)):
        print(matriz[i])
    return matriz[-1][-1]


print(mochila(3, 5, [1, 2, 3], [6, 10, 12])) # -> 22
#print(mochila(3, 5, [3, 2, 1], [12, 10, 6])) # -> 22