def remove_duplicate(string):
    letras_dict = {}
    for letra in string:
        if letra not in letras_dict:
            letras_dict[letra] = 1
        else:
            letras_dict[letra] += 1
    print(letras_dict)
    min = 'z'
    resultado = []
    for letra in string:
        print(min)
        resultado.append(letra)
        if letra < min:
            min = letra
        if min in letras_dict:
            resultado.remove(min)
            
    print(resultado)

print(remove_duplicate('bcabc')) # -> abc
print(remove_duplicate('cbacdcbc')) # -> acdb
