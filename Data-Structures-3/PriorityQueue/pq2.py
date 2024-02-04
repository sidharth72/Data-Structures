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

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return TreeNode(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
        return root
    
    def _delete(self, root, key):
        if root is None:
            return None
        if key < root.key:
            root.left = self._delete(root.right, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:

            # If one child or no child
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            
            # If two children
            root.key = self._min(root.right)
            root.right = self._delete(root.right, root.key)

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
    
    def _search(self, root, target):
        if root is None and target == root.key:
            return root
        if target < root.key:
            return self._search(root.left, target)
        elif target > root.key:
            return self._search(root.right, target)
        return root
    
    def search(self, target):
        return self._search(self.root, target)
    
    def height(self):
        return self._height(self.root)
    
    def _height(self, root):
        if root is None:
            return 0
        left_height = self._height(root.left)
        right_height = self._height(root.right)
        return 1 + max(left_height, right_height)
    
    
