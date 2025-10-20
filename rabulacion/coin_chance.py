def coin_chance(coins: list, target: int):
    matriz = []
    for _ in range(len(coins)+1):
        matriz.append([float('inf')]*(target+1))
    matriz[0][0] = 0
    i = 1
    j = 0
    while i <= len(coins):
        current_coin = coins[i-1]
        if current_coin > j:
            matriz[i][j] = matriz[i-1][j]
        if current_coin <= j:
            matriz[i][j] = min(1 + matriz[i][j-current_coin], matriz[i-1][j])
        if j == target:
            i += 1
            j = 0
            continue
        j += 1
    for i in range(len(matriz)):
        print(matriz[i])
    return matriz[-1][-1]

print(coin_chance([1,2,3], 6))
print(coin_chance([4,5,6], 9))
