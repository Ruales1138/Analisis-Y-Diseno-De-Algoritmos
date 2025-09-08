# Definición de un nodo de árbol binario
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def all_possible_full_binary_trees(total_nodes):
    """
    Genera todos los árboles binarios llenos con exactamente 'total_nodes' nodos.
    Usa recursión con memorización para no recalcular soluciones.
    """
    memo = {}  # Guardará soluciones ya calculadas: memo[n] = lista de raíces posibles

    def build_trees(n):
        # Si ya calculamos este caso, lo retornamos
        if n in memo:
            return memo[n]

        # Caso base: con 1 nodo solo hay un árbol (la raíz sin hijos)
        if n == 1:
            return [TreeNode(0)]

        trees = []  # lista de árboles posibles con n nodos

        # Repartimos n-1 nodos entre el subárbol izquierdo y derecho
        for left_count in range(1, n, 2):  # solo números impares
            right_count = n - 1 - left_count

            # Generamos todas las combinaciones de subárboles
            left_subtrees = build_trees(left_count)
            right_subtrees = build_trees(right_count)

            for left in left_subtrees:
                for right in right_subtrees:
                    root = TreeNode(0)   # la raíz siempre tiene valor 0
                    root.left = left
                    root.right = right
                    trees.append(root)

        memo[n] = trees  # guardamos la solución para no recalcular
        return trees

    # Si el número de nodos es par, no se puede construir un árbol binario lleno
    if total_nodes % 2 == 0:
        return []

    return build_trees(total_nodes)

def serialize_tree(root):
    """
    Convierte un árbol binario en una lista usando recorrido por niveles (level-order).
    Usa 'null' en lugar de nodos vacíos.
    """
    if root is None:
        return []

    queue = [root]
    result = []

    while queue:
        node = queue.pop(0)  # sacamos el primer nodo de la cola

        if node is None:
            result.append("null")
        else:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)

    # Eliminar los "null" innecesarios del final
    while result and result[-1] == "null":
        result.pop()

    return result

def print_all_fbt_as_lists(n):
    """
    Genera e imprime todos los árboles binarios llenos con n nodos
    en formato lista estilo LeetCode.
    """
    trees = all_possible_full_binary_trees(n)
    for tree in trees:
        print(serialize_tree(tree))


# --- Ejemplo de uso ---
print_all_fbt_as_lists(7)
