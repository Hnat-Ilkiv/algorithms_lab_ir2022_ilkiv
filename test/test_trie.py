import unittest
from src.trie import Trie

class TestTrieMethods(unittest.TestCase):
    def test_insert_and_search(self):
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.search("apple"))
        self.assertFalse(trie.search("app"))
        self.assertFalse(trie.search("orange"))

    def test_starts_with_prefix(self):
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.starts_with_prefix("app"))
        self.assertFalse(trie.starts_with_prefix("ora"))

    def test_empty_trie(self):
        trie = Trie()
        self.assertFalse(trie.search("word"))
        self.assertFalse(trie.starts_with_prefix("pre"))

if __name__ == '__main__':
    unittest.main()

