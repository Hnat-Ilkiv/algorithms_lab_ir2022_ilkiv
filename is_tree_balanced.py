from binary_tree import BinaryTree
from display_ascii_tree import display_ascii_tree_horizontally

def check_balanced(node):
    if node is None:
        return 0

    left_height = check_balanced(node.left)
    if left_height == -1:
        return -1

    right_height = check_balanced(node.right)
    if right_height == -1:
        return -1

    if abs(left_height - right_height) > 1:
        return -1

    return max(left_height, right_height) + 1

def is_tree_balanced(node: BinaryTree) -> bool:
    return check_balanced(node) != -1


root = BinaryTree(50)
root.left = BinaryTree(17)
root.right = BinaryTree(76)
root.right.left = BinaryTree(54)
root.right.left.right = BinaryTree(72)
root.right.left.right.left = BinaryTree(67)

root.left.left = BinaryTree(9)
root.left.right = BinaryTree(23)
root.left.left.right = BinaryTree(14)
root.left.left.right.left = BinaryTree(12)
root.left.right.left = BinaryTree(19)

display_ascii_tree_horizontally(root)

print(is_tree_balanced(root))

root1 = BinaryTree(50)
root1.left = BinaryTree(17)

root1.right = BinaryTree(72)
root1.right.left = BinaryTree(54)
root1.right.left.right = BinaryTree(67)
root1.right.right = BinaryTree(76)

root1.left.left = BinaryTree(12)
root1.left.right = BinaryTree(23)
root1.left.left.right = BinaryTree(14)
root1.left.left.left = BinaryTree(9)
root1.left.right.left = BinaryTree(19)

display_ascii_tree_horizontally(root1)

print(is_tree_balanced(root1))
