def calcular_factorial(n: int, resultado = 1):
    if n == 1:
        return resultado
    resultado = resultado * n
    return calcular_factorial(n - 1, resultado)


print(calcular_factorial(5))