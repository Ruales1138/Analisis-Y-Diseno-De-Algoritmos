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
    return dp(n)

print(full_binary_trees(2)) # -> []
print(full_binary_trees(1)) # -> [0]
print(full_binary_trees(3)) # -> [[0,0,0]]
print(full_binary_trees(7)) # -> [[0,0,0,null,null,0,0,null,null,0,0],
                            #     [0,0,0,null,null,0,0,0,0],
                            #     [0,0,0,0,0,0,0],
                            #     [0,0,0,0,0,null,null,null,null,0,0],
                            #     [0,0,0,0,0,null,null,0,0]]