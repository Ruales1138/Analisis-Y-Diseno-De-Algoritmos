def subir_escaleras(n):
    lista = [1]*(n+1)
    i = 2
    while i <= 10:
        lista[i] = lista[i-1] + lista[i-2]
        i += 1
    print(lista)
    return lista[-1]

# print(subir_escaleras(2)) # ---> 2
# print(subir_escaleras(3)) # ---> 3
# print(subir_escaleras(4)) # ---> 5
# print(subir_escaleras(5)) # ---> 8
print(subir_escaleras(10)) # ---> 89