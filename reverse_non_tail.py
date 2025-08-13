def invertir_lista(lista: list) -> list:
    if len(lista) <= 1:
        return lista
    return [lista[-1]] + invertir_lista(lista[:-1])


print(invertir_lista([0,1,2,3,4,5]))
print(invertir_lista(['A', 'B', 'C', 'D']))