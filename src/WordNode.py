"""
Class of a word node, tracking the word (duh), the number of neighbors, and
which words this word is neighbors with.

Up to you if we need this or not.
"""


class WordNode():
    """docstring for WordNode"""
    def __init__(self, word):
        self.__word = word
        self.__neighbors = []

    def is_neighbor(self, other_word):
        """Returns true of the two words are different by one letter.

        :param other_word:  a string to compare to the current node's word
        :rtype : bool
        Returns: true if the words differ by one letter
        """
        differences = 0
        for i in range(len(self.__word)):
            if self.__word[i] != other_word[i]:
                differences += 1
        return differences == 1

    # Overloading isn't supported in python and apparently is very non-pythonic. Any ideas how to check if a wordnode
    # is neighbors with another node AND if it's neighbors with another node? Not that we NEED to, but it seems like
    # the logical way to do things (maybe that's just my java talking)

    # def is_neighbor(self, other_node):
    #     """Overload so that method works with strings and WordNodes"""
    #     return self.is_neighbor(other_node.get_word())

    def get_word(self):
        return self.__word

    def get_num_neighbors(self):
        return len(self.__neighbors)

    def get_neighbors(self):
        return self.__neighbors
