def sumar_elementos(lista: list[int], i: int = 0):
    if i == len(lista):
        return 0
    return lista[i] + sumar_elementos(lista, i+1)


lista = [1,4,6,2,8,3,8]
print(sumar_elementos(lista))