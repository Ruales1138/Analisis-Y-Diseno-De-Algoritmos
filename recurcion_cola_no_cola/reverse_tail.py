def invertir_lista(lista: list, lista_inv: list = [], i: int = 0, largo = None) -> list:
    if largo is None:
        largo = len(lista)
    if i == largo:
        return lista_inv
    lista_inv.append(lista.pop())
    return invertir_lista(lista, lista_inv, i + 1, largo)


print(invertir_lista([0,1,2,3,4,5], []))
print(invertir_lista([0,2,5,2,7,4], []))
print(invertir_lista(['A', 'B', 'C', 'D'], []))