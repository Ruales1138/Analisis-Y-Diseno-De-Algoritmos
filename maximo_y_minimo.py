def encontrar_mayor_y_menor(lista: list[int]) -> list[int]:
    if len(lista) == 0:
        return 0
    if len(lista) == 1:
        min = lista[0]
        max = lista[0]
        return min, max
    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]
    izquierda = encontrar_mayor_y_menor(izquierda)
    derecha = encontrar_mayor_y_menor(derecha)
    if izquierda[0] > derecha[0]:
        max = izquierda
    return izquierda, derecha


print(encontrar_mayor_y_menor([38, 27, 43, 3, 9, 82, 10])) 
print(encontrar_mayor_y_menor([4, 2, 7, 10]))             
print(encontrar_mayor_y_menor([]))             
print(encontrar_mayor_y_menor([5]))             
print(encontrar_mayor_y_menor([10, 9, 8, 7, 6]))             
print(encontrar_mayor_y_menor([3, 3, 3]))        