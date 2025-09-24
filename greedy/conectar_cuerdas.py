import heapq

def conectar_cuerdas(arr):
    heapq.heapify(arr)
    def recurcion(arr_cuerdas):
        if len(arr_cuerdas) > 1:
            cuerda_1 = heapq.heappop(arr_cuerdas)
            cuerda_2 = heapq.heappop(arr_cuerdas)
            return cuerda_1 + cuerda_2
        else:
            cuerda_1 = heapq.heappop(arr_cuerdas)
            return cuerda_1


    return recurcion(arr)


print(conectar_cuerdas([4, 3, 2, 6])) # -> 29
print(conectar_cuerdas([10])) # -> 0
