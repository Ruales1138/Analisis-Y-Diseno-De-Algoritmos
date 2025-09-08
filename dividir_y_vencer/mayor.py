def encontrar_mayor(lista: list[int]) -> list[int]:
    if len(lista) == 0:
        return 0
    if len(lista) == 1:
        return lista[0]
    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]
    izquierda = encontrar_mayor(izquierda)
    derecha = encontrar_mayor(derecha)
    if izquierda > derecha:
        return izquierda
    else:
        return derecha


print(encontrar_mayor([38, 27, 43, 3, 9, 82, 10])) 
print(encontrar_mayor([4, 2, 7, 10]))             
print(encontrar_mayor([]))             
print(encontrar_mayor([5]))             
print(encontrar_mayor([10, 9, 8, 7, 6]))             
print(encontrar_mayor([3, 3, 3]))        