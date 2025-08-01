lista = [3, 4, 5]

def posible_orden(lista, rta_actual = [], rtas = []):
    if len(rta_actual) == len(lista):
        copia = rta_actual.copy()
        rtas.append(copia)
        return rtas
    for op in lista:
        if op not in rta_actual:
            rta_actual.append(op)
            posible_orden(lista, rta_actual, rtas)
            rta_actual.pop()
    return rtas
            
print(posible_orden(lista))
