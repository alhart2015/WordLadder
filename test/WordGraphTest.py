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
        self.assertTrue(g.has_neighbor("beans"))
        self.assertFalse(g.has_neighbor("battle"))

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

    def test_path(self):
        g = WordGraph()
        g.add_word("beer")
        g.add_word("beef")
        g.add_word("bear")
        g.add_word("dear")
        g.add_word("beat")
        g.add_word("heat")
        g.add_word("hear")
        g.add_word("poop")
        print g.path("beef", "dear")
        print g.path("beef", "poop")
        self.assertTrue(g.path("heat", "beef") != [])
        self.assertFalse(g.path("poop", "hear"))

if __name__ == "__main__":
    unittest.main()
