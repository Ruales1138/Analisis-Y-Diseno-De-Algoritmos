def conteo(matriz, inicio = None, fin = None):
    if inicio is None:
        inicio = 0
    if fin is None:
        fin = len(matriz)
    mitad = (inicio + fin) // 2
    izquierda = matriz[inicio : mitad]
    derecha = matriz[mitad : fin]
    print(izquierda)
    print(derecha)
    c1 = []
    c2 = []
    c3 = []
    c4 = []
    for columna in izquierda:
        c1.append(columna[inicio : mitad])
    for columna in izquierda:
        c2.append(columna[mitad : fin])
    for columna in derecha:
        c3.append(columna[inicio : mitad])
    for columna in derecha:
        c4.append(columna[mitad : fin])
    print()
    print(c1, c2, c3, c4)
    
        
    
M_1 = [[1,2],
       [3,4]] 
M_2 = [[0]] 
M_3 = [[1,2,5,7],
       [8,9,7,2],
       [0,1,2,3],
       [4,6,1,8]]

print(conteo(M_1)) # → (suma=10, pares=2, impares=2)
print(conteo(M_2)) # → (0, 1, 0)
print(conteo(M_3)) # → ()