def encontrar_mayor_y_menor(lista: list[int]) -> list[int]:
    if len(lista) == 0:
        return ()
    if len(lista) == 1:
        menor = lista[0]
        mayor = lista[0]
        return mayor, menor
    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]
    izquierda = encontrar_mayor_y_menor(izquierda)
    derecha = encontrar_mayor_y_menor(derecha)
    return (min(izquierda[0], derecha[0]), max(izquierda[1], derecha[1]))

        
print(encontrar_mayor_y_menor([]))            
print(encontrar_mayor_y_menor([5]))        
print(encontrar_mayor_y_menor([15, 10]))
print(encontrar_mayor_y_menor([4, 2, 7, 10]))               
print(encontrar_mayor_y_menor([38, 27, 43, 3, 9, 82, 10])) 
print(encontrar_mayor_y_menor([10, 9, 8, 7, 6]))             
print(encontrar_mayor_y_menor([3, 3, 3]))