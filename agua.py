def capacidad_mayor(height):
    indices = []
    for i in range(len(height)):
        indices.append(i)
    height_ordenado = sorted(zip(height, indices), reverse=True)
    print(height_ordenado)
    mayor = 0
    for tupla in height_ordenado:
        for tupla_2 in height_ordenado:
            area = min(tupla[0], tupla_2[0]) * (tupla[1] - tupla_2[1])
            print(area)
            if area > mayor:
                mayor = area
    return mayor
    
    
print(capacidad_mayor([1,8,6,2,5,4,8,3,7])) # -> 49