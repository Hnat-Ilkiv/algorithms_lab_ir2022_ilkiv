"""
Implementation of Trie data structure.

Author: Hnat Ilkiv
Date: 2023-11-28
"""


class TrieNode:
    """
    Represents a node in the Trie.
    """

    def __init__(self):
        """
        Initialize a TrieNode.
        """
        self.children = {}
        self.is_end_of_word = False


class Trie:
    """
    Implementation of a Trie data structure.
    """

    def __init__(self):
        """
        Initialize a Trie.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Insert a word into the Trie.

        :param word: The word to insert.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        """
        Check if a word is present in the Trie.

        :param word: The word to search for.
        :return: True if the word is present, False otherwise.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with_prefix(self, prefix):
        """
        Check if there is any word in the Trie that starts with the given prefix.

        :param prefix: The prefix to check.
        :return: True if there is any word with the given prefix, False otherwise.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def prediction_words_with_prefix(self, prefix):
        """
        Get a list of words that can be obtained from the given prefix without using recursion.

        :param prefix: The prefix to use for predictions.
        :return: A list of words that can be obtained from the given prefix.
        """
        node = self.root

        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        stack = [(node, prefix)]
        words = []

        while stack:
            current_node, current_prefix = stack.pop()

            if current_node.is_end_of_word:
                words.append(current_prefix)

            for char, child_node in current_node.children.items():
                stack.append((child_node, current_prefix + char))

        return words


def print_trie_structure(node, prefix="", is_last=True):
    """
    Print the structure of the Trie.

    :param node: The current Trie node.
    :param prefix: The current prefix formed by traversing the Trie.
    :param is_last: True if the current node is the last child of its parent, False otherwise.
    """
    if prefix:
        indentation = "".join(
            char if char in [" ", "│"] else "" for char in prefix
        )
        print(f"{indentation}{'└─ ' if is_last else '├─ '}{prefix[-1]}")

    else:
        print("Root")

    children_count = len(node.children)
    for i, (char, child_node) in enumerate(node.children.items()):
        is_last_child = i == children_count - 1
        print_trie_structure(
            child_node,
            prefix + ("   " if is_last else "│  ") + char,
            is_last_child,
        )


if __name__ == "__main__":
    trie = Trie()
    words = [
        "able",
        "about",
        "above",
        "accept",
        "account",
        "across",
        "act",
        "action",
        "activity",
        "add",
        "address",
        "after",
        "afternoon",
        "again",
        "against",
        "age",
        "ago",
        "agree",
    ]
    words += ["tree", "trie", "true", "troops"]

    for word in words:
        trie.insert(word)

    # print(trie.prediction_words_with_prefix("ab"))
    # print(trie.prediction_words_with_prefix("tr"))

    print("Trie Structure:")
    print_trie_structure(trie.root)
