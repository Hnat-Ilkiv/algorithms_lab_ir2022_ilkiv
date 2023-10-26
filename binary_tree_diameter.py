from binary_tree import BinaryTree
from display_ascii_tree import display_ascii_tree_horizontally

def display_path_diameter(path_to_node1, path_to_node2):
    i = 0
    while i < len(path_to_node1) and i < len(path_to_node2) and path_to_node1[i] == path_to_node2[i]:
        i += 1
    root = [path_to_node1[i-1]]
    left = path_to_node1[:i-1:-1]
    right = path_to_node2[i:]
    path = left + root + right
    element_list = [element.value for element in path]
    display_path = " -> ".join(map(str,element_list))

    print(f"Branch diameter: {display_path}")

def find_path_to_node(node, target, path):
    if node is None:
        return False

    path.append(node)

    if node.value == target:
        return True

    if (node.left and find_path_to_node(node.left, target, path)) or (node.right and find_path_to_node(node.right, target, path)):
        return True

    path.pop()
    return False

def find_path_length(root, node1, node2):
    path_to_node1 = []
    path_to_node2 = []

    if not find_path_to_node(root, node1, path_to_node1) or not find_path_to_node(root, node2, path_to_node2):
        return -1

    if path_to_node1[-1].left is None and path_to_node1[-1].right is None and path_to_node2[-1].left is None and path_to_node2[-1].right is None:
        i = 0
        while i < len(path_to_node1) and i < len(path_to_node2) and path_to_node1[i] == path_to_node2[i]:
            i += 1

        display_path_diameter(path_to_node1, path_to_node2)
        return len(path_to_node1) + len(path_to_node2) - 2 * i
    return -1

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

    print(f"Binary tree diameter: {find_path_length(root, 2, 9)}")
