def contar(matriz, conteo = [0,0,0]):
    for fila in matriz:
        for num in fila:
            conteo[0] +=num
            if num % 2 == 0:
                conteo[1] += 1
            else:
                conteo[2] += 1
    return conteo

def contar_matriz(matriz, conteo = [0,0,0]):
    def contar_filas(fila, i = 0):
        fila[0]
        
    

M_1 = [[1,2],
       [3,4]] 
M_2 = [[0]] 

print(contar(M_1)) # → (suma=10, pares=2, impares=2)
print(contar(M_2)) # → (0, 1, 0)

#print(prueba([2,5,7,2]))