def contar(lista, inicio = None, fin = None):
    if inicio is None:
        inicio = 0
    if fin is None:
        fin = len(lista)-1
    if inicio > fin:
        return
    mitad = (inicio + fin) // 2
    izquierda = contar(lista, inicio, mitad)
    

print(contar([0,1,4,7,3,6,7,3]))