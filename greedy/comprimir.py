import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__(self):
        return str(self.val)   

def comprimir(string, valores=None, nuevo_nodo=None):
    if valores is None:
        frecuencia = {}
        for letra in string:
            if letra not in frecuencia:
                frecuencia[letra] = 1
            else:
                frecuencia[letra] += 1
        valores = []
        for clave, valor in frecuencia.items():
            valores.append((valor, clave))
        heapq.heapify(valores)
    if len(valores) > 1:
        valor_1 = heapq.heappop(valores)
        valor_2 = heapq.heappop(valores)
        if valor_1[1] == '*':
            nodo_1 = nuevo_nodo
        else:
            nodo_1 = TreeNode(valor_1)
        if valor_2[1] == '*':
            nodo_2 = nuevo_nodo
        else:
            nodo_2 = TreeNode(valor_2)
        suma = valor_1[0] + valor_2[0]
        nuevo_valor = (suma, '*')
        nuevo_nodo = TreeNode(nuevo_valor)
        nuevo_nodo.left = nodo_1
        nuevo_nodo.right = nodo_2
        heapq.heappush(valores, nuevo_valor)
        return comprimir(string, valores, nuevo_nodo)
    else:
        return nuevo_nodo
    
def print_tree(node, prefix="", is_left=True):
    if node is not None:
        print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.val))
        print_tree(node.left, prefix + ("    " if is_left else "│   "), True)

arbol_1 = comprimir('ABDDDCABCADAA')
print()
print_tree(arbol_1)
arbol_2 = comprimir('BCAADDDCCACACAC')
print()
print_tree(arbol_2)

def codificar(arbol, nodo_actual=None, ruta_actual=[], rutas=[]):
    if nodo_actual is None:
        nodo_actual = arbol
    if nodo_actual.left:
        ruta_actual.append(0)
        codificar(nodo_actual.left)
        ruta_actual.pop()
    if nodo_actual.right:
        ruta_actual.append(1)
        codificar(nodo_actual.right)
        ruta_actual.pop()
    if not nodo_actual.left and not nodo_actual.right:
        print('aaa')
        copia = ruta_actual.copy()
        rutas.append(copia)
        print(rutas)
        ruta_actual = []

print(codificar(arbol_1))