import math


class TreeNode:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def is_bst(root, min_val = -math.inf, max_val = math.inf):
    if root is None:
        return True
    
    if not min_val < root.key < max_val:
        return False
    
    return is_bst(root.left, min_val, root.key) and is_bst(root.right, root.key, max_val)




# Creating a larger Binary Search Tree
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(12)
root.right.right = TreeNode(18)

print(is_bst(root))