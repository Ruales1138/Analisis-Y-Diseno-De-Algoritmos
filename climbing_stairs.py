# from functools import lru_cache
# @lru_cache

def subir_escaleras(n, memo = {1:1, 2:2}):
    if n in memo:
        return memo[n]
    memo[n] = subir_escaleras(n-1) + subir_escaleras(n-2)
    return memo[n]

print(subir_escaleras(2)) # ---> 2
print(subir_escaleras(3)) # ---> 3
print(subir_escaleras(4)) # ---> 5
print(subir_escaleras(5)) # ---> 8