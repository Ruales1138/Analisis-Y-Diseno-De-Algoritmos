def calcular_fibonacci(n: int, lista: list = [0, 1]):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return calcular_fibonacci(n-1) + calcular_fibonacci(n-2)

print(calcular_fibonacci(10))