def verificar_palindromo(palabra: str, i: int = None, j: int = None) -> bool:
    if i is None and j is None:
        i = 0
        j = len(palabra) - 1
    if i == j:
        return True
    if i > j:
        return True
    if palabra[i] != palabra[j]:
        return False
    return verificar_palindromo(palabra, i + 1, j - 1)
    

print(verificar_palindromo('ada'))          # True
print(verificar_palindromo('ollo'))         # True
print(verificar_palindromo('oso'))          # True
print(verificar_palindromo('reconocer'))    # True
print(verificar_palindromo('radar'))        # True
print(verificar_palindromo('nivel'))        # False
print(verificar_palindromo('hola'))         # False
print(verificar_palindromo('python'))       # False
