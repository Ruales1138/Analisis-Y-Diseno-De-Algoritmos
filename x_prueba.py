from collections import deque  # Para usar una cola en el recorrido por niveles

# Clase para definir un nodo del árbol binario
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val      # valor del nodo
        self.left = left    # hijo izquierdo
        self.right = right  # hijo derecho

# Clase con la función principal
class Solution:
    def sortedArrayToBST(self, nums):
        # Función recursiva que construye el árbol
        def construir_arbol(inicio, fin):
            # Caso base: si ya no hay elementos en este rango
            if inicio > fin:
                return None
            
            # Tomamos el índice de en medio (para balancear el árbol)
            mid = (inicio + fin) // 2  # usa el centro izquierdo en caso de empate
            
            # Creamos el nodo raíz con el valor central
            nodo = TreeNode(nums[mid])
            
            # Construimos recursivamente el subárbol izquierdo
            nodo.left = construir_arbol(inicio, mid - 1)
            
            # Construimos recursivamente el subárbol derecho
            nodo.right = construir_arbol(mid + 1, fin)
            
            return nodo  # retornamos el nodo creado
        
        # Llamamos la función recursiva desde el rango completo
        return construir_arbol(0, len(nums) - 1)

# Función para mostrar el árbol en nivel-orden (como en LeetCode)
def imprimir_nivel_orden(root):
    if not root:
        return []
    
    resultado = []             # Aquí guardamos el recorrido
    cola = deque([root])       # Cola para recorrer el árbol nivel por nivel
    
    while cola:
        nodo = cola.popleft()  # Sacamos el primer nodo de la cola
        if nodo:
            resultado.append(nodo.val)  # Guardamos su valor
            cola.append(nodo.left)      # Metemos el hijo izquierdo (puede ser None)
            cola.append(nodo.right)     # Metemos el hijo derecho (puede ser None)
        else:
            resultado.append(None)      # Si el nodo no existe, guardamos None
    
    # Eliminamos los None sobrantes al final (para que quede bonito como en LeetCode)
    while resultado and resultado[-1] is None:
        resultado.pop()
    
    return resultado


# --------------------------
# Ejemplo de uso
# --------------------------
nums = [-10, -3, 0, 5, 9]
sol = Solution()
raiz = sol.sortedArrayToBST(nums)

# Imprimimos en nivel-orden
print("Nivel-orden:", imprimir_nivel_orden(raiz))
