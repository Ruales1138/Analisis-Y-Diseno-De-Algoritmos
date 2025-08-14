def separa_letras_non_tail(palabra: str, i = 0, vocales = 0, consonantes = 0):
    if i == len(palabra):
        return [vocales, consonantes]
    if palabra[i] in 'aeiou':
        vocales += 1
    else:
        consonantes += 1
    resultado = separa_letras_non_tail(palabra, i+1, vocales, consonantes)
    print(resultado[0])
    if resultado[0] > resultado[1]:
        return 'Vocales: ' + str(resultado[0])
    else:
        return resultado[1]



    
print(separa_letras_non_tail('aeiou'))
print(separa_letras_non_tail('aeisgfg'))


