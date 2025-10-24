def mochila(n: int, w: int, weights: list, values: list):
    lista = [0]*(w+1)
    print(lista)
    i_l = 1
    i_c = 0
    while i_c < n:
        current_weight = weights[i_c]
        current_value = values[i_c]
        print('i',i_l)
        print('w',current_weight)
        print('v',current_value)
        if current_weight <= i_l:
            new = current_value + lista[i_l-current_weight]
            if new > lista[i_l]:
                lista[i_l] = new
        print(lista)
        print()
        if i_l == w:
            i_l = 1
            i_c += 1
            continue
        i_l += 1
    print(lista)
    return lista[-1]

print(mochila(3, 5, [1, 2, 3], [6, 10, 12])) # -> 30
print(mochila(3, 5, [3, 2, 1], [12, 10, 6])) # -> 30