import pprint

def subsecuencia(string_1, string_2):
    matriz = []
    for _ in range(len(string_2)+1):
        matriz.append([0]*(len(string_1)+1))
    i = 1
    j = 1
    while i <= len(string_2):
        if string_1[j-1] == string_2[i-1]:
            matriz[i][j] = 1 + matriz[i-1][j-1]
        else:
            matriz[i][j] = max(matriz[i-1][j], matriz[i][j-1])
        if j == len(string_1):
            i += 1
            j = 1
            continue
        j +=1
    pprint.pp(matriz)
    return matriz[-1][-1]

print(subsecuencia('cancelar', 'ganar')) # -> 4
print(subsecuencia('hola', 'aoglnua')) # -> 3
print(subsecuencia('hola', 'cocacola')) # -> 3
print(subsecuencia('hola', 'carlos')) # -> 1