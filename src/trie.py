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


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))  # True
    print(trie.search("app"))  # False
    print(trie.starts_with_prefix("app"))  # True
