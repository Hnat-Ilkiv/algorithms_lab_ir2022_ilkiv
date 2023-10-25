class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"value = {self.value};"

    def __str__(self):
        return f"Value: {self.value}"
