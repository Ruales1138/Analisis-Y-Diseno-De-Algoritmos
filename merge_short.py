def merge(izquierda: list[int], derecha: list[int]) -> list[int]:
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    if i == len(izquierda):
        resultado.extend(derecha[j:])
    if j == len(derecha):
        resultado.extend(izquierda[i:])
    return resultado

def merge_sort(lista: list[int]) -> list[int]:
    if len(lista) <= 1:
        return lista
    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]
    izquierda = merge_sort(izquierda)
    derecha = merge_sort(derecha)
    return merge(izquierda, derecha)


print(merge_sort([38, 27, 43, 3, 9, 82, 10]))   # → [3, 9, 10, 27, 38, 43, 82]
print(merge_sort([4, 2, 7, 1]))                 # → [1, 2, 4, 7]
print(merge_sort([]))                           # → []
print(merge_sort([5]))                          # → [5]
print(merge_sort([10, 9, 8, 7, 6]))             # → [6, 7, 8, 9, 10]
print(merge_sort([3, 3, 3]))                    # → [3, 3, 3]