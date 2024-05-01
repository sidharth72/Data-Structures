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
            return root
        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)

        else:

            # If only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
                
            # If two childs
            root.key = self._min(root.right)
            root.right = self._delete(root.right, root.key)

        return root
    
    def _min(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current.key

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, root, result):
        if root:
            self._inorder(root.left, result)
            result.append(root.key)
            self._inorder(root.right, result)

    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, root, result):
        if root:
            result.append(root.key)
            self._preorder(root.left, result)
            self._preorder(root.right, result)

    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, root, result):
        if root:
            self._postorder(root.left, result)
            self._postorder(root.right, result)
            result.append(root.key)

    def height(self):
        return self._height(self.root)


    def _height(self, root):
        if root is None:
            return 0
        left_height = self._height(root.left)
        right_height = self._height(root.right)
        return 1 + max(left_height, right_height)
    
    def _depth(self, root):
        if root is None:
            return -1
        left_depth = self._depth(root.left)
        right_depth = self._depth(root.right)
        return 1 + max(left_depth, right_depth)
    
    def search(self, target):
        value = self._search(self.root, target)
        if value is None:
            return "Not found"
        return value.key
    
    def _search(self, root, target):
        if root is None or root.key == target:
            return root
        if target < root.key:
            return self._search(root.left, target)
        else:
            return self._search(root.right, target)
        

    def is_perfect(self):
        height = self._height(self.root)
        return self._is_perfect(self.root, height, 0)
    
    def is_complete(self):
        height = self._height(self.root)
        return self._is_complete(self.root, height, 0)
    
    def is_full(self):
        return self._is_full(self.root)

    def _is_perfect(self, root, height, level):
        if root is None:
            return True
        
        # If leaf node, we'll need to check if the height of the tree stands with the level since 
        # In a perfect tree, the leaf nodes are in the same level
        if root.left is None and root.right is None:
            return height == level + 1
        
        if root.left is None or root.right is None:
            return False
        
        return (self._is_perfect(root.left, height, level + 1) and
                self._is_perfect(root.right, height, level + 1))
    
    def _is_complete(self, root, height, level):
        # If there is no root, then the subtree is complete
        if root is None:
            return True
        
        # If the current level is the second last level and any node at this level has a missing child 
        # (either left or right), then the subtree is not complete
        if level == height - 1 and (root.left is None or root.right is None):
            return False
        # Recursively check the completeness of left and right subtrees, incrementing the level
        if level < height - 1:
            return (self._is_complete(root.left, height, level + 1) and
                    self._is_complete(root.right, height, level + 1))
        # If all conditions are met, the subtree is complete
        return True

    def _is_full(self, root):
        # if root is none, then it is full binary tree
        if root is None:
            return True
        # if both left and right root is none, it is a leaf, and if that is the case, it is a full binary tree
        if root.left is None and root.right is None:
            return True
        # If both left and right roots have 2 childs both, then it will recursively check if 
        # That is same for all the other roots in left and right subtree, it not, it will return false
        if root.left is not None and root.right is not None:
            return (self._is_full(root.left) and self._is_full(root.right))
        return False


tree = BinaryTree()

tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(5)

print(tree.inorder())
print(tree.preorder())
print(tree.postorder())

print(tree.height())

print(tree.search(100))


