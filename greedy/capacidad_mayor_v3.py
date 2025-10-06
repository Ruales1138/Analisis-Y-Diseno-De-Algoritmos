def capacidad_mayor(alturas):
    inicio = 0
    fin = len(alturas)-1
    maximo = 0
    while inicio < fin:
        inicio_altura = alturas[inicio]
        fin_altura = alturas[fin]
        area = min(inicio_altura, fin_altura) * (fin - inicio)
        if area > maximo:
            maximo = area
        inicio += 1
    return maximo


print(capacidad_mayor([1,8,6,2,5,4,8,3,7]))