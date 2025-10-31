def conbinaciones(n: int, lista_letras: list = ['a','e','i','o','u'], respuesta: str = '', lista_respuestas: list = []):
    if len(respuesta) == n:
        lista_respuestas.append(respuesta)
        return lista_respuestas
    for letra in lista_letras:
        conbinaciones(n, lista_letras, respuesta+letra, lista_respuestas)
    return lista_respuestas

#print(len(conbinaciones(4)))
print(conbinaciones(2))
