import unittest
from WordNode import WordNode


class WordNodeTest(unittest.TestCase):

    def test_neighbor(self):
        node = WordNode("beer")
        yes = WordNode("deer")
        no = WordNode("bend")
        self.assertTrue(node.is_neighbor("deer"))
        self.assertFalse(node.is_neighbor("bend"))

if __name__ == "__main__":
    unittest.main()

