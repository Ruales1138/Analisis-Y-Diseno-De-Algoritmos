def mochila(val, wt, capacity):
    objetos = sorted(zip(wt, val))
    print(objetos)
    def mochila_recurcion(objetos, capacity, i=0):
        if i == len(objetos):
            return 0
        objeto = objetos[i]
        valor = objeto[1]
        peso = objeto[0]
        print(objeto)
        if capacity - peso == 0:
            return valor
        if capacity - peso > 0:
            return valor + mochila_recurcion(objetos, capacity-peso, i+1)
        else:
            return mochila_recurcion(objetos, capacity, i+1)
    return mochila_recurcion(objetos, capacity)

val = [60, 100, 120] 
wt = [10, 20, 30] 
capacity = 50

val_2 = [500] 
wt_2 = [30] 
capacity_2 = 10

print(mochila([20, 15], [10, 5], 30))
print(mochila(val, wt, capacity)) # -> 240
print(mochila(val_2, wt_2, capacity_2)) # -> 166.667