def capacidad_mayor(alturas, inicio=None, fin=None, maximo = 0):
    if inicio is None:
        inicio = 0
        fin = len(alturas)-1
    if inicio == len(alturas) or fin < 0 or inicio > fin:
        return maximo
    inicio_altura = alturas[inicio]
    fin_altura = alturas[fin]
    area = min(inicio_altura, fin_altura) * (fin - inicio)
    if area > maximo:
        maximo = area
    if inicio_altura < fin_altura:
        return capacidad_mayor(alturas, inicio+1, fin, maximo)
    else:
        return capacidad_mayor(alturas, inicio, fin-1, maximo)
    
print(capacidad_mayor([1,8,6,2,5,4,8,3,7]))