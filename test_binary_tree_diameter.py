from binary_tree import BinaryTree
from binary_tree_diameter import binary_tree_diameter

import unittest

class TestBinaryTreeDiameter(unittest.TestCase):
    def setUp(self):
        self.root = BinaryTree(1)
        self.root.left = BinaryTree(3)
        self.root.right = BinaryTree(2)
        self.root.left.left = BinaryTree(7)
        self.root.left.right = BinaryTree(4)
        self.root.left.left.left = BinaryTree(8)
        self.root.left.left.left.left = BinaryTree(9)
        self.root.left.right.right = BinaryTree(5)
        self.root.left.right.right.right = BinaryTree(6)

    def test_binary_tree_diameter(self):
        self.assertEqual(binary_tree_diameter(self.root), 6)

if __name__ == '__main__':
    unittest.main()
