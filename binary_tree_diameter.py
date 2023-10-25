from binary_tree import BinaryTree
from display_ascii_tree import display_ascii_tree_horizontally

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
        current, depth, path = queue.pop(0)
        if current.left:
            queue.append((current.left, depth + 1, path + [current.left]))
        if current.right:
            queue.append((current.right, depth + 1, path + [current.right]))
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
    print(f"Binary branch: {get_path(path_node.left)[::-1] + [path_node] + get_path(path_node.right)}")

    return diameter



if __name__ == "__main__":
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
