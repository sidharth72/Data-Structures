class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

def is_complete(root, index, nodes_count):
    if root is None:
        return True
    if index >= nodes_count:
        return False
    
    return (is_complete(root.left, 2 * index + 1, nodes_count)
            and is_complete(root.right, 2 * index + 2, nodes_count))

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

total_nodes = count_nodes(root)

if is_complete(root, 0, total_nodes):
    print("The binary tree is complete")
else:
    print("The binary tree is not complete")