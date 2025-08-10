def calcular_fibonacci(n: int, i: int = 2, lista: list[int] = [0, 1]):
    if i == n:
        return lista[-1]
    lista.append(lista[-1] + lista[-2])
    lista.pop(0)
    return calcular_fibonacci(n, i+1, lista)

print(calcular_fibonacci(10))
    