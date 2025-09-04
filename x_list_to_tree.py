class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def construir_arbol(nums, inicio = None, fin = None):
    if inicio is None:
        inicio = 0
    if fin is None:
        fin = len(nums)-1
    if inicio > fin:
        return
    mitad = (inicio + fin) // 2
    nodo = TreeNode(nums[mitad])
    nodo.left = construir_arbol(nums, inicio, mitad-1)
    nodo.right = construir_arbol(nums, mitad+1, fin)
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


nums = [-10, -3, 0, 5, 9]
nodo = construir_arbol(nums)
print(imprimir_arbol(nodo))