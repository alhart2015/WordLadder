'''
Class to represent  a dictionary as a graph. Nodes = words, two words have an
edge between them if they are separated by one letter (eg. beer, bear).
'''

class WordGraph():
    """Graph of words with above rules. Represents the graph as an adjacency
    list."""
    def __init__(self):
        self.__words = []

    def __str__(self):
      return "Words: %s" % (self.__words)
