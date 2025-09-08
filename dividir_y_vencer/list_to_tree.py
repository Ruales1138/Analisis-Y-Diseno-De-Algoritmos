class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.val)
        
def print_tree(node, prefix="", is_left=True):
    if node is not None:
        print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.val))
        print_tree(node.left, prefix + ("    " if is_left else "│   "), True)
        
def crear_arbol(lista, inicio = None, fin = None):
    if inicio is None:
        inicio = 0
    if fin is None:
        fin = len(lista)-1
    if inicio > fin:
        return
    mitad = (inicio + fin) // 2
    nodo = TreeNode(lista[mitad])
    nodo.left = crear_arbol(lista, inicio, mitad-1)
    nodo.right = crear_arbol(lista, mitad+1, fin)
    return nodo

def imprimir_arbol(raiz):
    if raiz is None:
        return []
    resultado = []
    cola = [raiz]
    while cola:
        nodo = cola.pop(0)
        if nodo:
            resultado.append(nodo.val)
            cola.append(nodo.left)
            cola.append(nodo.right)
        else:
            resultado.append(None)
    while resultado[-1] is None:
        resultado.pop()
    return resultado


nodo = crear_arbol(list(range(1,15)))
print(print_tree(nodo))
print(imprimir_arbol(nodo))