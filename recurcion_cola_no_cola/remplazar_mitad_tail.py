def remplazar_mitad(string, inicio=None, fin=None):
    if inicio is None:
        inicio = 0
    if fin is None:
        fin = len(string) - 1
    if inicio == fin:
        return string
    if string[inicio].isdigit() and string[fin].isdigit():
        largo = fin - inicio + 1
        if largo % 2 == 0:
            mitad = inicio + (largo // 2)
            return string.replace(string[mitad], '0')
        else:
            return string
    if string[inicio].isdigit():
        return remplazar_mitad(string, inicio, fin - 1)
    else:
        return remplazar_mitad(string, inicio + 1, fin)

print(remplazar_mitad('a1234b'))
