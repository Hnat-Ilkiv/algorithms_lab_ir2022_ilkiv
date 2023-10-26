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

def max_path(node):
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

def display_path_diameter(node):
    root = [node]
    left = max_path(node.left)[::-1] if node.left else []
    right = max_path(node.right) if node.right else []
    path = left + root + right
    element_list = [element.value for element in path]
    display_path = " -> ".join(map(str,element_list))

    print(f"Branch diameter: {display_path}")


def binary_tree_diameter(tree: BinaryTree) -> int:
    if not tree:
        return 0

    diameter = 0
    path_node = None
    queue = [tree]

    while queue:
        node = queue.pop(0)

        left_height = max_depth(node.left)
        right_height = max_depth(node.right)

        if left_height != 0 and right_height:
            current_diameter = left_height + right_height

            if current_diameter > diameter:
                path_node = node

            diameter = max(diameter, current_diameter)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    if path_node is None:
        return 0

    print(f"Top diameter: {path_node.value}")
    display_path_diameter(path_node)

    return diameter



if __name__ == "__main__":
    root = BinaryTree(1)
    root.left = BinaryTree(3)
    # root.right = BinaryTree(2)
    root.left.left = BinaryTree(7)
    # root.left.right = BinaryTree(4)
    root.left.left.left = BinaryTree(8)
    root.left.left.left.left = BinaryTree(9)
    # root.left.right.right = BinaryTree(5)
    # root.left.right.right.right = BinaryTree(6)

    print("Display binary tree:")
    display_ascii_tree_horizontally(root)

    print(f"Binary tree diameter: {binary_tree_diameter(root)}")
