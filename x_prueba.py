import heapq

# Crear una lista y convertirla en min-heap
arr = [5, 3, 8, 1]
heapq.heapify(arr)   # O(n)
print(arr)  # [1, 3, 8, 5] (orden interno de heap, no necesariamente ordenado)

smallest = heapq.heappop(arr)   # O(log n)
print(smallest)  # 1
print(arr)       # [3, 5, 8]


smallest = heapq.heappop(arr)  
print(smallest)  # 1
print(arr)   