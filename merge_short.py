def merge_sort(lista: list[int]) -> list[int]:
    if len(lista) == 0:
        return lista


print(merge_sort([38, 27, 43, 3, 9, 82, 10]))   # → [3, 9, 10, 27, 38, 43, 82]
print(merge_sort([4, 2, 7, 1]))                 # → [1, 2, 4, 7]
print(merge_sort([]))                           # → []
print(merge_sort([5]))                          # → [5]
print(merge_sort([10, 9, 8, 7, 6]))             # → [6, 7, 8, 9, 10]
print(merge_sort([3, 3, 3]))                    # → [3, 3, 3]