def contar(lista, inicio_fila = None, fin_fila = None, inicio_columna = None, fin_columna = None):
    if fin_columna is None:
        inicio_fila = 0
        fin_fila = len(lista)-1
        inicio_columna = 0
        fin_columna = len(lista)-1
    if inicio_fila == fin_fila and inicio_columna == fin_columna:
        num = lista[inicio_fila][inicio_columna]
        if num % 2 == 0:
            return (num, 1, 0)
        else:
            return (num, 0, 1)
    mitad_fila = (inicio_fila + fin_fila) // 2
    mitad_columna = (inicio_columna + fin_columna) // 2
    c1 = contar(lista, inicio_fila, mitad_fila, inicio_columna, mitad_columna)
    c2 = contar(lista, inicio_fila, mitad_fila, mitad_columna+1, fin_columna)
    c3 = contar(lista, mitad_fila+1, fin_fila, inicio_columna, mitad_columna)
    c5 = contar(lista, mitad_fila+1, fin_fila, mitad_columna+1, fin_columna)
    suma = c1[0] + c2[0] + c3[0] + c5[0]
    pares = c1[1] + c2[1] + c3[1] + c5[1]
    impares = c1[2] + c2[2] + c3[2] + c5[2]
    return (suma, pares, impares)
   
print(contar([[1,2,3,4],  # -> (136,8,8)
              [5,6,7,8],
              [9,10,11,12],
              [13,14,15,16]]))