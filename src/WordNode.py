"""
Class of a word node, tracking the word (duh), the number of neighbors, and
which words this word is neighbors with.

Up to you if we need this or not.
"""


class WordNode():
    """docstring for WordNode"""
    def __init__(self, word):
        self.word = word
        self.neighbors = []

    def is_neighbor(self, other_word):
        """Returns true of the two words are different by one letter.

        Parameter: word, a string to compare to the current node's word
        Returns: true if the words differ by one letter
        """
        for i in range(len(self.word)):
            if self.word[i] != other_word[i]:
                return False
        return True

    def is_neighbor(self, other_node):
        """Overload so that method works with strings and WordNodes"""
        return self.is_neighbor(other_node.get_word())

    def get_word(self):
        return self.word

    def get_num_neighbors(self):
        return len(self.neighbors)

    def get_neighbors(self):
        return self.neighbors
