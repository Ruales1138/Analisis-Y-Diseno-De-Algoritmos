def remove_duplicate(string):
    letras_dict = {}
    for letra in string:
        if letra not in letras_dict:
            letras_dict[letra] = 1
        else:
            letras_dict[letra] += 1
    min = string[0]
    resultado = []
    print(letras_dict)
    print(resultado)
    print(min)
    for letra in string:
        letras_dict[letra] -= 1
        if letra not in resultado:
            resultado.append(letra)
        else:
            if resultado[0] == letra:
                resultado.remove(letra)
                resultado.append(letra)
        if letra < min:
            if letras_dict[min] > 0:
                resultado.remove(min)
            min = letra
        print(resultado)
        print(min)
    return resultado

print(remove_duplicate('bcabc')) # -> abc
print('----------------')
print(remove_duplicate('cbacdcbc')) # -> acdb
print('----------------')
print(remove_duplicate('bacbcacc')) # -> abc
