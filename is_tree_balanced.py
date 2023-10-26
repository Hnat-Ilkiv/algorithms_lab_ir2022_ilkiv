from binary_tree import BinaryTree
from display_ascii_tree import display_ascii_tree_horizontally

def check_balanced(node):
    if node is None:
        return 0

    left_height = check_balanced(node.left)
    # print(node,"\tleft", left_height)
    if left_height == -1:
        return -1

    right_height = check_balanced(node.right)
    # print(node,"\tright", right_height)
    if right_height == -1:
        return -1
    # print(node, "\t\tbal", left_height - right_height)
    if abs(left_height - right_height) > 1:
        return -1
    # print(node,"\t\t\treturn", max(left_height, right_height) + 1)
    return max(left_height, right_height) + 1

def is_tree_balanced(node: BinaryTree) -> bool:
    return check_balanced(node) != -1


root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)
root.right.left = BinaryTree(15)
root.right.right = BinaryTree(7)

display_ascii_tree_horizontally(root)

print(is_tree_balanced(root))
