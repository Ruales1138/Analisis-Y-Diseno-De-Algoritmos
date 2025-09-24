def mochila(val, wt, capacity):
    valor_por_kilo = []
    for i in range(len(val)):
        valor_por_kilo.append(val[i] / wt[i])
    objetos = sorted(zip(valor_por_kilo, val, wt), reverse=True)
    def mochila_recurcion(objetos, capacity, i=0):
        if i == len(objetos):
            return 0
        objeto = objetos[i]
        valor = objeto[1]
        peso = objeto[2]
        if capacity - peso == 0:
            return valor
        if capacity - peso > 0:
            return valor + mochila_recurcion(objetos, capacity-peso, i+1)
        else:
            fraccion = capacity/peso
            return valor * fraccion
    return mochila_recurcion(objetos, capacity)

val = [60, 100, 120] 
wt = [10, 20, 30] 
capacity = 50

val_2 = [500] 
wt_2 = [30] 
capacity_2 = 10

print(mochila(val, wt, capacity)) # -> 240
print(mochila(val_2, wt_2, capacity_2)) # -> 166.667