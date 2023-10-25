from binary_tree import BinaryTree
from display_ascii_tree import display_ascii_tree_horizontally

def max_depth_recursive(node):
    if not node:
        return 0
    return 1 + max(max_depth_recursive(node.left), max_depth_recursive(node.right))

def binary_tree_diameter_recursive(tree: BinaryTree) -> int:
    if not tree:
        return 0

    left_height = max_depth_recursive(tree.left)
    right_height = max_depth_recursive(tree.right)

    left_diameter = binary_tree_diameter_recursive(tree.left)
    right_diameter = binary_tree_diameter_recursive(tree.right)

    return max(left_height + right_height, max(left_diameter, right_diameter))


def max_depth(node):
    if not node:
        return 0

    queue = [(node, 1)]

    while queue:
        current, depth = queue.pop(0)
        if current.left:
            queue.append((current.left, depth + 1))
        if current.right:
            queue.append((current.right, depth + 1))
    return depth

def get_path(node):
    if not node:
        return 0

    queue = [(node, 1, [node])]

    while queue:
        # print(f"\tЧерга старт: {queue}")
        current, depth, path = queue.pop(0)
        # print(f"\t\tЕлемент: {current}, Глибина :{depth}, Шлях: {path};")
        if current.left:
            # print(f"\t\tLeft:")
            # path.append(current.left)
            # print(f"\t\t\tpath = {path}")
            queue.append((current.left, depth + 1, path + [current.left]))
            # print(f"\t\t\tqueue = {queue}")
            # print(f"\t\tpath.pop = {path.pop()}")
        # print(f"\t\tЧерга проміжок: {queue}")
        if current.right:
            # print(f"\t\tRight:")
            # path.append(current.right)
            # print(f"\t\t\tpath = {path}")
            queue.append((current.right, depth + 1, path + [current.right]))
            # print(f"\t\t\tqueue = {queue}")
            # print(f"\t\tpath.pop = {path.pop()}")
        # print(f"\t\tЧерга фініш: {queue}")
    return path



def binary_tree_diameter(tree: BinaryTree) -> int:
    if not tree:
        return 0

    diameter = 0
    path_node = None
    queue = [tree]

    while queue:
        node = queue.pop(0)
        get_path(node)

        left_height = max_depth(node.left)
        right_height = max_depth(node.right)

        current_diameter = left_height + right_height
        if current_diameter > diameter:
            path_node = node

        diameter = max(diameter, current_diameter)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    print(path_node)

    return diameter



if __name__ == "__main__":
    # Створення тестового бінарного дерева
    root = BinaryTree(1)
    root.left = BinaryTree(3)
    root.right = BinaryTree(2)
    root.left.left = BinaryTree(7)
    root.left.right = BinaryTree(4)
    root.left.left.left = BinaryTree(8)
    root.left.left.left.left = BinaryTree(9)
    root.left.right.right = BinaryTree(5)
    root.left.right.right.right = BinaryTree(6)

    print("Display binary tree:")
    display_ascii_tree_horizontally(root)

    print(f"Binary tree diameter: {binary_tree_diameter(root)}")
