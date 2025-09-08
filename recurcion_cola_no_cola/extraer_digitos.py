def extraer_digitos(texto, numeros = [], index = None):
    if index == len(texto):
        if len(numeros) > 1:
            numero_1 = numeros[0]
            numero_2 = numeros[-1]
            return numero_1 + numero_2
        else:
            return
    if index is None:
        index = 0
    letra = texto[index]
    if letra.isdigit():
        numeros.append(letra)
    return extraer_digitos(texto, numeros, index + 1)

def separar_lista(lista, index = None, lista_numeros = []):
    if index == len(lista):
        return lista_numeros
    if index is None:
        index = 0
    texto = lista[index]
    respuesta = extraer_digitos(texto, [])
    if respuesta is not None:
        lista_numeros.append(respuesta)
    return separar_lista(lista, index + 1, lista_numeros)
    

entrada = ["abc7x3t4z", "def23", "hello", "9a1b2", "g5h"]
#print(extraer_digitos(entrada[0]))
print(separar_lista(entrada))



    
    
    
    
    