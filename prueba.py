def merge_sort(lista):
    # Si la lista tiene 0 o 1 elementos, ya está ordenada
    if len(lista) <= 1:
        return lista
    
    # Dividir la lista en dos mitades
    medio = len(lista) // 2
    izquierda = lista[:medio]
    derecha = lista[medio:]
    
    # Ordenar cada mitad recursivamente
    izquierda = merge_sort(izquierda)
    derecha = merge_sort(derecha)
    print(izquierda)
    print(derecha)
    return
    
    # Combinar las dos mitades ordenadas
    #return merge(izquierda, derecha)

# def merge(izquierda, derecha):
#     resultado = []
#     i = j = 0
    
#     # Comparar elementos de izquierda y derecha, agregando el menor primero
#     while i < len(izquierda) and j < len(derecha):
#         if izquierda[i] < derecha[j]:
#             resultado.append(izquierda[i])
#             i += 1
#         else:
#             resultado.append(derecha[j])
#             j += 1
    
#     # Agregar los elementos restantes (si los hay)
#     resultado.extend(izquierda[i:])
#     resultado.extend(derecha[j:])
    
#     return resultado


# Ejemplo de uso
datos = [34, 7, 23, 32, 5, 62, 32, 7]
print(datos)
print()
print(merge_sort(datos))
