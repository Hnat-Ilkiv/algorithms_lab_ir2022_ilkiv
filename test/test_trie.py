"""
Module containing unit tests for the Trie class.

Author: Hnat Ilkiv
Date: 2023-11-28
"""

import unittest
from src.trie import Trie


class TestTrieMethods(unittest.TestCase):
    """
    Class for testing the methods of the Trie class.
    """

    def test_insert_and_search(self):
        """
        Test inserting words into the trie and searching for them.
        """
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.search("apple"))
        self.assertFalse(trie.search("app"))
        self.assertFalse(trie.search("orange"))

    def test_starts_with_prefix(self):
        """
        Test checking if the trie contains words starting with a given prefix.
        """
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.starts_with_prefix("app"))
        self.assertFalse(trie.starts_with_prefix("ora"))

    def test_empty_trie(self):
        """
        Test searching in an empty trie.
        """
        trie = Trie()
        self.assertFalse(trie.search("word"))
        self.assertFalse(trie.starts_with_prefix("pre"))

    def test_prediction_words_with_prefix(self):
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
            "tree",
            "trie",
            "true",
            "troops",
        ]

        for word in words:
            trie.insert(word)

        ab = ["above", "about", "able"]
        ac = [
            "act",
            "activity",
            "action",
            "across",
            "account",
            "accept",
        ]
        tr = ["troops", "true", "trie", "tree"]
        full = [
            "troops",
            "true",
            "trie",
            "tree",
            "agree",
            "ago",
            "age",
            "again",
            "against",
            "after",
            "afternoon",
            "add",
            "address",
            "act",
            "activity",
            "action",
            "across",
            "account",
            "accept",
            "above",
            "about",
            "able",
        ]

        self.assertEqual(trie.prediction_words_with_prefix("ab"), ab)
        self.assertEqual(trie.prediction_words_with_prefix("ac"), ac)
        self.assertEqual(trie.prediction_words_with_prefix("tr"), tr)
        self.assertEqual(trie.prediction_words_with_prefix("app"), [])
        self.assertEqual(trie.prediction_words_with_prefix(""), full)


if __name__ == "__main__":
    unittest.main()
