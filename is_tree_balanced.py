class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_tree_balanced(node: BinaryTree) -> bool:
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

    return check_balanced(node) != -1


# Приклад використання
root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)
root.right.left = BinaryTree(15)
root.right.right = BinaryTree(7)

print(is_tree_balanced(root))  # Повинно вивести True
