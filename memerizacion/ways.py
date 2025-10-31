def ways(lista: list[list[int]], memo: dict = None, i: int = 0, j: int = 0):
    if memo is None:
        memo = {}
        n = len(lista)-1
        m = len(lista[0])-1
        memo[(n, m)] = 1
    if (i,j) in memo:
        return memo[(i,j)]
    if i == len(lista):
        return 0
    if j == len(lista[0]):
        return 0
    if lista[i][j] == 1:
        return 0
    memo[(i,j)] = ways(lista, memo, i+1, j) + ways(lista, memo, i, j+1)
    return memo[(i,j)]


grid = [[0,0,0],
        [0,1,0],
        [0,0,0]]
print(ways(grid)) # ---> 2