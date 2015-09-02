"""
Class to represent  a dictionary as a graph. Nodes = words, two words have an
edge between them if they are separated by one letter (eg. beer, bear).
"""


class WordGraph():
    """Graph of words with above rules. Represents the graph as an adjacency
    list."""

    def __init__(self):
        self.__graph = {}

    def path(self, word, other):
        """Finds a path between word and other. If there is no path, returns an empty list.

        Gotta do some graph search algorithm I guess...

        :type word: basestring
        :param word: one of the end words

        :type other: basestring
        :param other: the other end word

        :rtype list of strings
        """
        pass

    def add_word(self, word):
        """Adds a word to the graph. If the word is already in the graph, does nothing.

        :type word: string
        :param word: the string to add to the graph
        """
        if word in self.__graph:
            return
        self.__graph[word] = set()

        for w in self.__graph.keys():
            if self.is_neighbor(word, w):
                self.__graph[word].add(w)
                self.__graph[w].add(word)

    def is_neighbor(self, word, other):
        """Returns true of the two words are different by one letter.

        This definitely should be static, but isn't everything supposed to be a class method when you're unit testing?

        :param word: a string to compare to other
        :param other:  a string to compare to the word
        :rtype : bool
        """
        differences = 0
        for i in range(len(word)):
            if differences > 1:
                return False
            if word[i] != other[i]:
                differences += 1
        return differences == 1

    def __contains__(self, item):
        if item in self.__graph.keys():
            return True
        return False

    def __str__(self):
        out = ""
        for word in self.__graph.keys():
            out += word
            out += ": "
            for neighbor in self.__graph[word]:
                out += neighbor
                out += " "
            out += "\n"
        return out
