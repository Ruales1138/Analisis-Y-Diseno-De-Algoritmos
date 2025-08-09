def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0] 
    menores = []
    mayores = []
    for elemento in lista[1:]:
        if elemento <= pivote:
            menores.append(elemento)
        if elemento > pivote:
            mayores.append(elemento)
    return quick_sort(menores) + [pivote] + quick_sort(mayores)


datos = [34, 7, 23, 32, 5, 62, 32, 7]
print(quick_sort(datos))