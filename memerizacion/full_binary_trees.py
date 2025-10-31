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

def full_binary_trees(n):
    if n % 2 == 0:
        return []
    memo = {}
    def dp(n):
        if n in memo:
            return memo[n]
        if n == 1:
            return [TreeNode(0)]
        trees = []
        for left_count in range(1, n, 2):
            right_count = n-1-left_count
            left = full_binary_trees(left_count)
            right = full_binary_trees(right_count)
            for l in left:
                for r in right:
                    root = TreeNode(0)
                    root.left = l
                    root.right = r
                    trees.append(root)
        memo[n] = trees
        return memo[n]
    return dp(n)

# print(full_binary_trees(11)) # -> []
# print(full_binary_trees(2)) # -> []
# print(full_binary_trees(1)) # -> [0]
# print(full_binary_trees(3)) # -> [[0,0,0]]
# print(full_binary_trees(7)) # -> [[0,0,0,null,null,0,0,null,null,0,0],
                            #     [0,0,0,null,null,0,0,0,0],
                            #     [0,0,0,0,0,0,0],
                            #     [0,0,0,0,0,null,null,null,null,0,0],
                            #     [0,0,0,0,0,null,null,0,0]]
nodos = full_binary_trees(7)
for n in nodos:
    print_tree(n)