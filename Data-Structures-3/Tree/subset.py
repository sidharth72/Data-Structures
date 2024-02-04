class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_subset(bst1, bst2):

    def inorder(node, result):
        if node:
            inorder(node.left, result)
            result.append(node.value)
            inorder(node.right, result)

    bst1_inorder = []
    bst2_inorder = []

    inorder(bst1, bst1_inorder)
    inorder(bst2, bst2_inorder)

    i, j = 0, 0

    # While both BST traversal is completed
    while i < len(bst1_inorder) and j < len(bst2_inorder):

        # If the value of the left subtree is less than the value of the right subtree
        if bst1_inorder[i] < bst2_inorder[j]:
            i += 1 # Then we need to iterate the main tree again to check further
        elif bst1_inorder[i] == bst2_inorder[j]: # If we find a value equal in both trees, in the same position
            i += 1 # Then increment j in the second sub BST
            j += 1 # Tne incement i in the first main BST
            # To check if both are in the same order and the values are same, 
        else:
            return False

    # The catch is that if all the nodes are processed in the main tree, i will be equal to len(bst1 main)
        # WHich means the second tree is the subset of the first main tree, because all the nodes are processed
    return i == len(bst1_inorder)


# Example usage:
# Create BSTs
bst_X = TreeNode(10)
bst_X.left = TreeNode(5)
bst_X.right = TreeNode(15)
bst_X.left.left = TreeNode(2)
bst_X.left.right = TreeNode(7)

bst_Y = TreeNode(5)
bst_Y.left = TreeNode(2)
bst_Y.right = TreeNode(7)

result = is_subset(bst_Y, bst_X)
print(result)