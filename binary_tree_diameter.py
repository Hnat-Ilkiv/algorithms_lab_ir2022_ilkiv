from binary_tree import BinaryTree
from display_ascii_tree import display_ascii_tree_horizontally

def max_depth(node):
    if not node:
        return 0
    return 1 + max(max_depth(node.left), max_depth(node.right))

def binary_tree_diameter(tree: BinaryTree) -> int:
    if not tree:
        return 0

    left_height = max_depth(tree.left)
    right_height = max_depth(tree.right)

    left_diameter = binary_tree_diameter(tree.left)
    right_diameter = binary_tree_diameter(tree.right)

    return max(left_height + right_height, max(left_diameter, right_diameter))

if __name__ == "__main__":
    # Створення тестового бінарного дерева
    root = BinaryTree(0)

    root.left = BinaryTree(1)
    root.right = BinaryTree(2)

    root.left.left = BinaryTree(3)
    root.left.right = BinaryTree(4)
    root.right.left = BinaryTree(5)
    root.right.right = BinaryTree(6)

    root.left.left.left = BinaryTree(7)
    root.left.left.right = BinaryTree(8)
    root.left.right.left = BinaryTree(9)
    root.left.right.right = BinaryTree(10)
    root.right.left.left = BinaryTree(7)
    root.right.left.right = BinaryTree(8)
    root.right.right.left = BinaryTree(9)
    root.right.right.right = BinaryTree(10)

    root.left.left.left.left = BinaryTree(9)
    root.left.right.right.right = BinaryTree(6)

    display_ascii_tree_horizontally(root)

    print(binary_tree_diameter(root))
