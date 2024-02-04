# Binary Tree
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
        if root is None: # Insert until the root it None
            return TreeNode(key)
        if key < root.key:
            # root.left and root.right are none, so using recursion, the new node is created
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
        return root
    
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result
    
    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result

    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result
    
    def _inorder(self, root, result):
        if root:
            self._inorder(root.left, result)
            result.append(root.key)
            self._inorder(root.right, result)

    def _preorder(self, root, result):
        if root:
            result.append(root.key)
            self._preorder(root.left, result)
            self._preorder(root.right, result)

    def _postorder(self, root, result):
        if root:
            self._postorder(root.left, result)
            self._postorder(root.right, result)
            result.append(root.key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:

            return root
        
        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            # If one or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            # If two childs
            root.key = self._min_value(root.right)
            root.right = self._delete(root.right, root.key)

        return root

    # Given the right target value as node, we need to traverse from there to the left for finding the minimum value
    def _min_value(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.key
    



tree = BinaryTree()

tree.insert(6)
tree.insert(4)
tree.insert(2)
tree.insert(5)
tree.insert(7)
tree.insert(9)

tree.delete(4)

# tree.delete(4)
# tree.delete(7)

print(tree.inorder())
print(tree.preorder())
print(tree.postorder())