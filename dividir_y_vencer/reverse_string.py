def invertir(palabra: list[int]) -> list[int]:
    if len(palabra) <= 1:
        return palabra
    mitad = len(palabra) // 2
    izquierda = palabra[:mitad]
    derecha = palabra[mitad:]
    izquierda = invertir(izquierda)
    derecha = invertir(derecha)
    return derecha + izquierda


print(invertir("abcd"))
print(invertir("a"))