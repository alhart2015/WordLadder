"""
Class to represent  a dictionary as a graph. Nodes = words, two words have an
edge between them if they are separated by one letter (eg. beer, bear).
"""


class WordGraph:
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
        if word in self.__graph.keys():
            return self.depth_first_search(word, other)

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
        # Remove this if we want to match words with different lengths?
        if len(word) is not len(other):
            return False

        differences = 0
        for i in range(len(word)):
            if differences > 1:
                return False
            if word[i] != other[i]:
                differences += 1
        return differences == 1

    def has_neighbor(self, word):
        """Returns true if the word has any neighbors"""
        if word not in self.__graph.keys():
            return False
        return len(self.__graph[word]) > 0

    def neighbors(self, word):
        """Returns the neighbors of the word"""
        return self.__graph[word]

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

    def depth_first_search(self, start, end):
        """Vanilla depth first search. Tryna do this without googling, see if I remember any of my schooling from 6
        months ago.

        :type start: basestring
        :param start: the first node in the search

        :type end: basestring
        :param end: the word you're searching for

        :rtype a list of strings in the path
        """
        return self.dfs_helper(start, end, [], set())

    def dfs_helper(self, start, end, path, visited):
        # You found it
        if start == end:
            path.append(end)
            return path

        visited.add(start)

        # Check all the neighbors
        for other in self.__graph[start]:
            if other not in visited:
                path.append(start)
                return self.dfs_helper(other, end, path, visited)

