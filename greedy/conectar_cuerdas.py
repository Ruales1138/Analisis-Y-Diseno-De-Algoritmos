import heapq

def conectar_cuerdas(arr):
    heapq.heapify(arr)
    def recurcion(arr_cuerdas):
        if len(arr_cuerdas) > 1:
            cuerda_1 = heapq.heappop(arr_cuerdas)
            cuerda_2 = heapq.heappop(arr_cuerdas)
            costo = cuerda_1 + cuerda_2
            heapq.heappush(arr_cuerdas, costo)
            return costo + recurcion(arr_cuerdas)
        else:
            return 0
    return recurcion(arr)

print(conectar_cuerdas([4, 3, 2, 6])) # -> 29
print(conectar_cuerdas([10])) # -> 0
