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


print(encontrar_mayor("abcd")) 
print(encontrar_mayor("a"))   