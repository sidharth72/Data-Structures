class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None



def is_balanced(root):

    def height_and_balanced(node):
        if not node:
            return 0,  True

        left_height, left_balanced = height_and_balanced(node.left)
        right_height, right_balanced = height_and_balanced(node.right)

        balance_factor = left_height - right_height
        node_balanced = abs(balance_factor) <= 1
        node_height = max(left_height, right_height) + 1
        overall_balanced = node_balanced and right_balanced and left_balanced
        return node_height, overall_balanced

    _, is_balanced = height_and_balanced(root)
    return is_balanced




root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(12)

print(is_balanced(root))