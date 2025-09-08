def calcular_factorial(n: int) -> int:
    if n == 1:
        return 1
    return n * calcular_factorial(n - 1)


print(calcular_factorial(5))