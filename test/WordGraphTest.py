import unittest
from WordGraph import WordGraph


class WordGraphTest(unittest.TestCase):
    def test_add(self):
        g = WordGraph()
        g.add_word("beans")
        g.add_word("bears")
        g.add_word("beets")
        g.add_word("battlestar galactica")
        g.add_word("beats")
        print g

    def test_neighbor(self):
        g = WordGraph()
        word = "beer"
        other = "bend"
        third = "deer"
        self.assertTrue(g.is_neighbor(word, third))
        self.assertFalse(g.is_neighbor(word, other))

    def test_contains(self):
        g = WordGraph()
        g.add_word("beer")
        self.assertFalse("beef" in g)
        self.assertTrue("beer" in g)

if __name__ == "__main__":
    unittest.main()
