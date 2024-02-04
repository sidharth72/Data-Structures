class TreeNode:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return TreeNode(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
        return root
    
    def inorder(self):

        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, root, result):
        if root:
            self._inorder(root.left, result)
            result.append(root.key)
            self._inorder(root.right, result)

tree = BinaryTree()

tree.insert(4)
tree.insert(9)
tree.insert(1)
tree.insert(3)
tree.insert(2)
tree.insert(8)
tree.insert(11)

print(tree.inorder())