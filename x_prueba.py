def contar(lista, inicio = None, fin = None):
    if inicio is None:
        inicio = 0
    if fin is None:
        fin = len(lista)-1
    if inicio > fin:
        return
    if inicio == fin:
        num = lista[inicio]
        if num % 2 == 0:
            return (num, 1, 0)
        else:
            return (num, 0, 1)
    mitad = (inicio + fin) // 2
    izquierda = contar(lista, inicio, mitad)
    derecha = contar(lista, mitad+1, fin)
    suma = izquierda[0] + derecha[0]
    pares = izquierda[1] + derecha[1]
    impares = izquierda[2] + derecha[2]

    return (suma, pares, impares)
    

print(contar([1,2,3,4,5,6]))