from binary_tree import BinaryTree

def display_ascii_tree_horizontally(root, prefix=""):
    if root is None:
        print("Tree is empty.")
        return

    if root.right:
        display_ascii_tree_horizontally(root.right, prefix + "    ")

    print(prefix + "--" + str(root.value))

    if root.left:
        display_ascii_tree_horizontally(root.left, prefix + "    ")


def display_ascii_tree_vertically(root):
    if not root:
        return []

    result = []
    this_level = [root]
    result.append(this_level)
    while this_level:
        next_level = []
        for node in this_level:
            if node:
                print(node)
                next_level.append(node.left)
                next_level.append(node.right)
            else:
                # next_level.append(None)
                # next_level.append(None)
                pass

        # result.append(this_level)
        print(f"this_level: {this_level}\tnext_level: {next_level}")
        this_level = next_level
    print(result)

if __name__ == "__main__":
    # Створення тестового бінарного дерева
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)


    # Вивід бінарного дерева в консоль
    display_ascii_tree_horizontally(root)

    # Вивід бінарного дерева вертикально в консоль у вигляді ASCII-арт
    # display_ascii_tree_vertically(root)
