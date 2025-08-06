def sumar_elementos(lista: list[int], i: int = 0, resultado: int = 0):
    if i == len(lista):
        return resultado
    resultado += lista[i]
    return sumar_elementos(lista, i+1, resultado)


lista = [1,4,6,2,8,3,8]
print(sumar_elementos(lista))