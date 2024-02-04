class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def is_balanced(root):
    def height_and_balance(node):
        if not node:
            return 0, True
        
        left_height, left_balanced = height_and_balance(node.left)
        right_height, right_balanced = height_and_balance(node.right)

        balance_factor = left_height - right_height
        node_balanced = abs(balance_factor) <= 1

        node_height = max(left_height, right_height) + 1

        overall_balanced = node_balanced and left_balanced and right_balanced

        return node_height, overall_balanced
    
    node_height, is_tree_balanced = height_and_balance(root)
    return node_height, is_tree_balanced


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(is_balanced(root))